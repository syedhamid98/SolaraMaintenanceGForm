if __name__ == '__main__':
    from selenium import webdriver
    from cpuinfo import get_cpu_info
    #from multiprocessing import freeze_support
    import webbrowser, os, socket ,cpuinfo, platform, psutil, shutil, time

    # Format in KB, MB, GB, TB
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    # Open Browser for Solara Maintenance Checklist
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScumeHQ4hKEzneEmj_Aax6YIb8ZBecpJxrVLSASARcKw587Nw/viewform'
    web = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    web.get(url)

    # Hostname
    uname = platform.uname()
    hostnamebox = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    hostnamebox.send_keys(uname.node)

    # IP Address
    host_name = socket.gethostname() 
    IPAddress = socket.gethostbyname(host_name)
    IPbox = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    IPbox.send_keys(IPAddress)

    # CPU
    cpuBrand = cpuinfo.get_cpu_info()['brand_raw']
    cpuBox = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cpuBox.send_keys(cpuBrand)

    # RAM Information
    svmem = psutil.virtual_memory()
    ramBox = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ramBox.send_keys(get_size(svmem.total))

    # HDD
    total, used, free = shutil.disk_usage("/")
    hddBox = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')
    hddBox.send_keys(total // (2**30), "GB")

    # Check Box
    checAV = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[2]/label[1]/div/div').click()
    winUpdate = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[4]/label[1]/div/div').click()
    tweakTool = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[6]/label[1]/div/div').click()
    diskCleanup = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[8]/label[1]/div/div').click()
    checkDisk = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[10]/label[1]/div/div').click()
    NoAppStartup = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[12]/label[1]/div/div').click()
    removeBloatware = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[14]/label[1]/div/div').click()
    externalCondition = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[16]/label[1]/div/div').click()
    cleanHeatsink = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[18]/label[3]/div/div').click()
    updateApplication = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[20]/label[1]/div/div').click()
    labelDevice = web.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[22]/label[3]/div/div').click()

    time.sleep(30)