# import sys
# import locale
# import subprocess
# import threading

# # copied from https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/Main/install.py#L37
# def handle_stream(stream, is_stdout):
#     stream.reconfigure(encoding=locale.getpreferredencoding(), errors='replace')

#     for msg in stream:
#         if is_stdout:
#             print(msg, end="", file=sys.stdout)
#         else: 
#             print(msg, end="", file=sys.stderr)

# # copied from https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/Main/install.py#L37
# def process_wrap(cmd_str, cwd=None, handler=None):
#     print(f"[Impact Pack] EXECUTE: {cmd_str} in '{cwd}'")
#     process = subprocess.Popen(cmd_str, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

#     if handler is None:
#         handler = handle_stream

#     stdout_thread = threading.Thread(target=handler, args=(process.stdout, True))
#     stderr_thread = threading.Thread(target=handler, args=(process.stderr, False))

#     stdout_thread.start()
#     stderr_thread.start()

#     stdout_thread.join()
#     stderr_thread.join()

#     return process.wait()

# pip_install = [sys.executable, "-s", "-m", "pip", "install"]

# process_wrap(pip_install + ['-r', 'requirements.txt'], cwd=__file__)