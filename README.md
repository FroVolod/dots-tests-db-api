Usage
1. Install Python 3.5 or newer

2. Install extra project modules buy issuing the following command from the terminal:

      cd "C:\path\to\the\project\folder"
      
      pip install -r requirements.txt
  
3. Configure the payment and delivery information in config.py file

4. В первом окне терминала запустить проект:

      $ python main.py

5. Во втором окне терминала выполнить запрос:

      curl -u admin:admin -i http://127.0.0.1:5000/tests/qwe.pdf
