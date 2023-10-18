print('''
    * VS Code Extensions: 
      - NoteBook [.ipynb] : Jupyter, Jupytar KeyMap, Jupyter NoteBook Render      
      - Icons:  Vscode-icons, Matrial Theme icons
      - Themes: Jellyfish, GitHub themes, 
      - GitHub:  Github copilot (Free For GitHub Student Plan), Codium (Free), Blackbox AI 
      - Code Formatter: Prettier
      - Markdown [keyboard shortcuts] : Markdown All In One
      - Code [Take a beautiful Code Screenshot]: CodeSnap
      
      ''')

print('''
* Mini Conda: As talked earlier, Conda provides an environments (like different rooms, spaces, directories to run different tools)
      
      - Install Mini Coonda software.
      - Install Conda VS Extention
      - Ctrl+J to open the Toogle Panel. A terminal will open as PowerShell environment (base). 
      - Press + and select the Command Prompt, to create an Environment . 
      - first, If we install MiniConda, then open it and run command : "conda env list" to show all the evironments, where only the base environment will exist; like (base) C:/user/.
      - ** check Conda CheetSheet online https://docs.conda.ai/projects/conda/ for codes
      - Now we are going to create new envirnoment, type the code in conda prompt >> conda create -n (env_name) like >> conda create -n python_eda
      - A new environment will created, to check type code >> conda env list (Enter) *All the envirnemnts will listed
      - Now enter to the newly cretaed environment, type code >> conda activate pythone_eda (Enter) *The python_eda envirnoment now activated
      - Now here a Step to Install Python under this environment. type code >> conda install python
      - Type >> conda list *To show/list all the install softwares under this environment of (pyhton_eda).
    
      
    Commands: 
      - conda list  # list all files/apps from current environment
      - conda env list  # list all environments
      - conda create -n environment_name    # -n for new. We can add the specific python version to install
      - For more, visit https://docs.conda.ai/projects/conda/

      # Assignmet:
      - How to Run envirnoment in VS Terminal 


      # Register on Poe.ai 
      - write a command prompt for python
      - paste the command in VS ipynb notebook in ptython_eda, hopefully it requires you to install the ipykernal extension.

      # We can install libraries in python using pip command
      - type >> pip install numPy sciPy matplotlib seaborn pandas plotly statsModels (Enter to install libraries under python_ead toolbox/room/envirnoment)
      - or we can install libraries from a file contating all the required packages for a project. This provides benifit to record the install libraries for future concern, when required runiining this project on another machine.
         First we create a .txt file i.e requirements.txt, then write the libraries names [Pandas, numpy, mypy, jupiter] each one on new line >> Now run this file from any file
         >> pip install -r requirements.txt 

      ''')

# Book to Read " Python for Data Analysis, 3E" https://wesmckinney.com/book/





