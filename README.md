# System Monitor

System Monitor is a Python utility for displaying real-time system information such as CPU usage, memory usage, disk usage, and network activity. It provides a command-line interface to view these metrics in a tabular format.

## Installation

You can install System Monitor from its GitHub repository using pip. Make sure you have Python and pip installed on your system.

pip install git+https://github.com/MrGengarnenok/system_monitor.git

## Usage

After installation, you can use the systeminfo command to display system information:

systeminfo

The systeminfo command outputs a table with metrics updated every 2 seconds.

## Adding systeminfo to PATH (Optional)

## Linux/macOS

    Open your terminal.

    Open your ~/.bashrc or ~/.bash_profile file using a text editor:

nano ~/.bashrc

# or

nano ~/.bash_profile

Add the following line at the end of the file:

export PATH="$PATH:/home/gengar/.local/bin"  # Replace with your installation path

Save the file and reload the shell configuration:

source ~/.bashrc  # or source ~/.bash_profile

## Windows

1. Open Control Panel.
2. Search for "Environment Variables" and click on "Edit the system environment variables".
3. In the System Properties window, click on "Environment Variables...".
4. Under "User variables" or "System variables", select the "Path" variable and click "Edit...".
5. Click "New" and add the path to your systeminfo executable (e.g., C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Scripts).
6. Click "OK" to save the changes.

Contributing

Contributions are welcome! If you want to contribute to System Monitor, follow these steps:

1. Fork the repository on GitHub.
2.  Clone your forked repository to your local machine. 
3.  Create a new branch for your feature or bug fix. M
4.  Make changes and commit them to your branch. P
5.  Push your changes to your fork on GitHub.
6.  Submit a pull request to the main branch of the original repository.

License

This project is licensed under the MIT License. See the LICENSE file for details.
