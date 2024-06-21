# System Monitor

System Monitor is a Python utility for displaying real-time system information such as CPU usage, memory usage, disk usage, and network activity. It provides a command-line interface to view these metrics in a tabular format.

## Installation

You can install System Monitor from its GitHub repository using pip. Make sure you have Python and pip installed on your system.

```bash
pip install git+https://github.com/MrGengarnenok/system_monitor.git

Usage

After installation, you can use the systeminfo command to display system information:

bash

systeminfo

The systeminfo command outputs a table with metrics updated every 2 seconds.
Adding systeminfo to PATH (Optional)

If the systeminfo command is not found after installation, you may need to add the installation directory to your PATH environment variable.
Linux/macOS

    Open your terminal.

    Open your ~/.bashrc or ~/.bash_profile file using a text editor:

    bash

nano ~/.bashrc
# or
nano ~/.bash_profile

Add the following line at the end of the file:

bash

export PATH="$PATH:/home/gengar/.local/bin"  # Replace with your installation path

Save the file and reload the shell configuration:

bash

    source ~/.bashrc  # or source ~/.bash_profile

Windows

    Open Control Panel.
    Search for "Environment Variables" and click on "Edit the system environment variables".
    In the System Properties window, click on "Environment Variables...".
    Under "User variables" or "System variables", select the "Path" variable and click "Edit...".
    Click "New" and add the path to your systeminfo executable (e.g., C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Scripts).
    Click "OK" to save the changes.

Now, you should be able to run systeminfo from any directory in your terminal or command prompt.
Contributing

Contributions are welcome! If you want to contribute to System Monitor, follow these steps:

    Fork the repository on GitHub.
    Clone your forked repository to your local machine.
    Create a new branch for your feature or bug fix.
    Make changes and commit them to your branch.
    Push your changes to your fork on GitHub.
    Submit a pull request to the main branch of the original repository.

License

This project is licensed under the MIT License. See the LICENSE file for details.
