import webbrowser
url1="www.youtube.com\watch?v=vLqahQVn_y4"
chromePath=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
webbrowser.get('chrome').open_new_tab(url1)