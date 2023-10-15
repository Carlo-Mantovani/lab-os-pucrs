#Authors: Aloysio Winter, Carlo Mantovani, Felipe Elsner, Lucas Cunha
#Modified: 09/13/2023
import time
from time import sleep
import sys
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class GetCpuLoad(object):


    def __init__(self, percentage=True, sleeptime=1):
        '''
        @parent class: GetCpuLoad
        @date: 04.12.2014
        @author: plagtag
        @info: 
        @param:
        @return: CPU load in percentage
        '''
        self.percentage = percentage
        self.cpustat = '/proc/stat'
        self.sep = ' '
        self.sleeptime = sleeptime

    def getcputime(self):
        cpu_infos = {}  # collect here the information
        with open(self.cpustat, 'r') as f_stat:
            lines = [line.split(self.sep) for content in f_stat.readlines()
                     for line in content.split('\n') if line.startswith('cpu')]

            # compute for every cpu
            for cpu_line in lines:
                if '' in cpu_line:
                    cpu_line.remove('')  # remove empty elements
                cpu_line = [cpu_line[0]]+[float(i) for i in cpu_line[1:]]  # type casting
                cpu_id, user, nice, system, idle, iowait, irq, softrig, steal, guest, guest_nice = cpu_line

                Idle = idle+iowait
                NonIdle = user+nice+system+irq+softrig+steal

                Total = Idle+NonIdle
                # update dictionionary
                cpu_infos.update({cpu_id: {'total': Total, 'idle': Idle}})
            return cpu_infos

    def getcpuload(self):
      
        start = self.getcputime()
        # wait a second
        sleep(self.sleeptime)
        stop = self.getcputime()

        cpu_load = {}

        for cpu in start:
            Total = stop[cpu]['total']
            PrevTotal = start[cpu]['total']

            Idle = stop[cpu]['idle']
            PrevIdle = start[cpu]['idle']
            CPU_Percentage = ((Total-PrevTotal)-(Idle-PrevIdle))/(Total-PrevTotal)*100
            cpu_load.update({cpu: CPU_Percentage})
        return cpu_load


HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8000


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        x = GetCpuLoad() # create object of class GetCpuLoad
        """Respond to a GET request."""
        datetime = os.popen('date').read()
        uptime = os.popen('awk \'{print $1}\' /proc/uptime').read()
        cpu_model = os.popen('cat /proc/cpuinfo | grep -i \'model\'').read()
        cpu_speed = os.popen('cat /proc/cpuinfo | grep -i \'cpu MHz\'').read()
        cpu_current_usage = x.getcpuload() # get cpu load
        mem_total_usage = os.popen('free | tr -s \' \' | cut -d\" \" -f2,3 | sed -n \'3!p\'').read()
        system_version = os.popen('cat /etc/os-release | grep -i \'version=\'').read()
        pid_name = os.popen('ps aux | tr -s \' \' | cut -d\" \" -f2,4').read()


        # Split the output into two values (model and model name) and ignore the headers
        cpu_model_lines = cpu_model.split('\n')
        cpu_model = cpu_model_lines[0]
        # remove "model" from the string
        cpu_model = cpu_model.replace("model", "")
        # remove the colon from the beginning of the string
        cpu_model = cpu_model[cpu_model.find(":") + 1:]

        cpu_model_name = cpu_model_lines[1]
        # remove "model name" from the string
        cpu_model_name = cpu_model_name.replace("model name", "")
        # remove the colon from the beginning of the string
        cpu_model_name = cpu_model_name[cpu_model_name.find(":") + 1:]

        # Organize the CPU load information into a table
        cpu_current_usage = str(cpu_current_usage)
        cpu_current_usage = cpu_current_usage.replace("{", "")
        cpu_current_usage = cpu_current_usage.replace("}", "")
        cpu_current_usage = cpu_current_usage.replace("'", "")
        cpu_current_usage = cpu_current_usage.replace(":", " ")
        cpu_current_usage = cpu_current_usage.replace(",", "\n")
        cpu_current_usage = cpu_current_usage.replace("cpu", "Core")
        cpu_current_usage_lines = cpu_current_usage.split("\n")
        cpu_usage_table = "<table border='1'><tr><th>CPU</th><th>Load</th></tr>"
        for i, line in enumerate(cpu_current_usage_lines):
            cpu, load = line.split()
            if i == 0:
                cpu = "Total"
            else:
                cpu = f"Core {i}"

            cpu_usage_table += f"<tr><td>{cpu}</td><td>{load}%</td></tr>"
        cpu_usage_table += "</table>"

       # Extract CPU speeds per core and organize them into a table
        cpu_speed_lines = cpu_speed.splitlines()
        core_info = []

        for i, line in enumerate(cpu_speed_lines):
            speed_value = line.split(":")[1].strip()
            core_name = f"Core {i + 1}"
            core_info.append(f"<tr><td>{core_name}</td><td>{speed_value} MHz</td></tr>")

        cpu_speed_table = "<table border='1'><tr><th>Core</th><th>Speed</th></tr>"
        cpu_speed_table += "\n".join(core_info)
        cpu_speed_table += "</table>"


        # Split the output into two values (total and used memory) and ignore the headers
        mem_lines = mem_total_usage.split('\n')
        mem_values = mem_lines[1].split()
        total_memory_kb, used_memory_kb = map(int, mem_values)

        # Convert KB to MB (1 KB = 1024 MB)
        total_memory_mb = total_memory_kb / 1024
        used_memory_mb = used_memory_kb / 1024
        total_memory_str = f"{total_memory_mb:.2f}"
        used_memory_str = f"{used_memory_mb:.2f}"

        # Split the PID and command info into rows
        pid_rows = pid_name.strip().split('\n')
        pid_rows.pop(0)  # Remove the first row (the column names)
        pid_table = "<table border='1'><tr><th>PID</th><th>Process</th></tr>"
        for row in pid_rows:
            pid, process = row.split(maxsplit=1)
            pid_table += f"<tr><td>{pid}</td><td>{process}</td></tr>"
        pid_table += "</table>"

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title><b>Target Machine Information</b>.</title></head>".encode())
        s.wfile.write(f"<p><b>Date and Time</b>: {datetime}</p>".encode())
        s.wfile.write(f"<p> <b>Uptime</b>: {uptime}s</p>".encode())
        s.wfile.write(f"<p> <b>CPU Model</b>: {cpu_model}</p>".encode())
        s.wfile.write(f"<p> <b>CPU Model Name</b>: {cpu_model_name}</p>".encode())
        s.wfile.write(f"<p> <h2><b>CPU Speed per Core</b></h2>{cpu_speed_table}</p>".encode())
        s.wfile.write(f"<p> <h2><b>CPU Load</b></h2> {cpu_usage_table}</p>".encode())
        s.wfile.write(f"<p> <b>Total Memory (MB)</b>: {total_memory_str}mb</p>".encode())
        s.wfile.write(f"<p> <b>Used Memory (MB)</b>: {used_memory_str}mb</p>".encode())
        s.wfile.write(f"<p> <b>System Version</b>: {system_version}</p>".encode())
        s.wfile.write(f"<p> <h2><b>PID and Process Name</b></h2>{pid_table}</p>".encode())
        s.wfile.write("</body></html>".encode())


if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print("Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))