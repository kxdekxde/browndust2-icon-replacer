# Brown Dust 2 Icon Replacer
A simple tool useful to mod [Brown Dust 2](https://www.browndust2.com/en-us/) icons. Thanks to Bingle for the help with this repacker.

## Requirements to use this tool:

  - Double-click on _Z_INSTALL_REQUIREMENTS.bat_ to install the required dependencies and Python 3.13.
  - Download and install [Microsoft C++ Build Tools](https://aka.ms/vs/17/release/vs_BuildTools.exe), and after that install the necessary dependencies following [this video](https://files.catbox.moe/vqsuix.mp4).


## Usage for modding:

1. Double-click on _Y___make_backup_before_update_game.py_ to copy the folder containing the file with the icons. The script will make a copy to the folder "Backup".
2. Double-click on _A___GET_RAW_FILES.bat_. This will run the scripts to get the raw files from the game folder and it will make a copy to the folder "Original Bundles".
3. Double-click on _0___EXTRACT_TEXTURES.bat_. This will extract the necessary textures with your modded icons.
4. Go to `\Extracted Assets\(icons folder)\(icons subfolder)` to see all the icons, from there you can start to mod them. After to finish your mods go back to the main directory of the tool.
4. Double-click on _0___PACK_IT.bat_. This will generate the new modded file for your modded icons.
5. Double-click on _0___REPLACE_IT.bat_. This will install the new generated file with your modded icons back in the game folder.
6. If everything worked you will see your modded icons when you launch your game.

Here a [Video Tutorial](https://files.catbox.moe/hzip8g.mp4).


NOTE: If you already modded the icons before then you will not get the original icons back unless you delete that game folder manually, that way the game will redownload the original file automatically the next time you launch the game. You can find the foldername opening the JSON file `illust.json` located in `\AddressablesJSON\GeneratedJSON` with Notepad.


## Usage to repack after game update:

1. Double-click on _Y___make_backup_before_update_game.py_ before to update your game if you already have mods located in the game folder. The script will make a backup of your mods to the folder "Backup" so you will not lose your mods when you update your game.
2. Update your game.
3. Double-click on _A___GET_RAW_FILES.bat_. This will run the scripts to get the raw files from the game folder and it will make a copy to the folder "Original Bundles".
4. Double-click on _0___EXTRACT_TEXTURES.bat_. This will extract the necessary textures with your modded icons.
5. Double-click on _0___PACK_IT.bat_. This will generate the new modded file for your modded icons.
6. Double-click on _0___REPLACE_IT.bat_. This will install the new generated file with your modded icons back in the game folder.
7. If everything worked you will see your modded icons working again when you launch your game.




Happy modding! ^‿^
