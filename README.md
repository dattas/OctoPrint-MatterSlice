# MatterSlice plugin for OctoPrint

## Setup

Install the plugin like you would install any regular Python package from source:

    pip install https://github.com/dattas/OctoPrint-MatterSlice/archive/master.zip
    
Make sure you use the same Python environment that you installed OctoPrint under, otherwise the plugin
won't be able to satisfy its dependencies.

Next you'll want to checkout and compile MatterSlice, please note you'll likely need to install `monodevelop` with your package manager along with `mono`

    git clone https://github.com/MatterHackers/MatterSlice.git
    cd ~/MatterSlice
    mozroots --import --sync
    mdtool build -c:Release MatterSlice.sln

Restart OctoPrint. `octoprint.log` should show you that the plugin was successfully found and loaded:

    2014-10-29 12:29:21,500 - octoprint.plugin.core - INFO - Loading plugins from ... and installed plugin packages...
    2014-10-29 12:29:21,611 - octoprint.plugin.core - INFO - Found 2 plugin(s): MatterSlice (0.1.0), Discovery (0.1)

## Configuration

After logging in, go to Settings, then MatterSlice. Ensure that the full path to mono is correct.

Put in the full path to your MatterSlice binary for example

    /home/octoprint/MatterSlice/bin/Release/MatterSlice.exe
Save!

Restart Octoprint to ensure it now thinks that MatterSlice can be used. You can then import your profile from matterslice and get slicing!
