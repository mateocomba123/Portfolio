# -*- coding: utf-8 -*-
"""
author: Mateio
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from datetime import date


def get_jobs(keyword, jobs_num, verbose, path, slp_time, intents):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(900, 700)
    
    jobs=[]
    pages = int(jobs_num / 30)  #Pages to scrap in total (total jobs vs jobs per page)
    page_num = 0 #set in 0 because the loop starts adding 1, this way it starts from the first one.
	
    while page_num < pages:
        page_num = page_num + 1
        intent = 1
        try:			
            while intent <= intents: #If true, should be still looking for new jobs.
                print("Page number " + str(page_num) + "/" + str(pages))
                print("Intent number in this page " + str(intent) + "/" + str(intents))
                try:
                    url = "https://www.glassdoor.com/Job/"+ keyword + "-jobs-SRCH_KO0,14_IP" + str(page_num) + ".htm?includeNoSalaryJobs=true"
                    driver.get(url)
			        #Let the page load. Change this number based on your internet speed.
			        #Or, wait until the webpage is loaded, instead of hardcoding it.
                    time.sleep(slp_time)
					
			
			        #Test for the "Sign Up" prompt and get rid of it.
                    try:
                        driver.find_element_by_css_selector("li[data-selected=true]").click()
                    except ElementClickInterceptedException:
                        pass
			
                    time.sleep(1)
			
                    try:
                        driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
                        #print(' x out worked')
                    except NoSuchElementException:
                        #print(' x out failed')
                        pass
			
			        
                    time.sleep(1)
					#Going through each job in this page
                    job_buttons = driver.find_elements_by_xpath('.//div//a[@class="jobLink"]')  #jl for Job Listing. These are the buttons we're going to click.
                    for job_button in job_buttons[0:30]:#Porque se encuentran mas elementos que no son jobs, entonces limito a esos primeros 30  
			
                        print("Progress: {}".format("" + str(len(jobs)+1) + "/" + str(jobs_num)))
                        #if len(jobs) >= num_jobs:
                            #break
                        time.sleep(1)
                        job_button.click()  #You might 
                        time.sleep(1)
                        collected_successfully = False
			            
                        while not collected_successfully:
                            try:
                                company_name = driver.find_element_by_xpath('.//div[@class="css-87uc0g e1tk4kwz1"]').text
                                location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz5"]').text
                                job_title = driver.find_element_by_xpath('.//div[contains(@class, "css-1vg6q84 e1tk4kwz4")]').text
                                job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                                #job_description = job_description.replace(',',' ')
                                collected_successfully = True
                            except:
                                time.sleep(3)
			
                        try:
                            salary_estimate = driver.find_element_by_xpath('.//span[@class="css-1imh2hq e1wijj242"]').text
                        except NoSuchElementException:
                            salary_estimate = -1 #You need to set a "not found value. It's important."
			            
                        try:
                            rating = driver.find_element_by_xpath('.//span[@class="css-19pjha7 e1cjmv6j1"]').text
                        except NoSuchElementException:
                            rating = -1 #You need to set a "not found value. It's important."
							
			            #Para estos atributos, hay que hacer un for
			            #Lo que hice fue encontrar todos, y asignarlos por orden a cada concepto
			            
                        try:
                            concepts = driver.find_elements_by_xpath('.//span[@class="css-1of40bq epgue5a0"]')
			            
                            puntajes = []
                            for concept in concepts[0:4]:
                                texto = concept.text
                                puntajes.append(texto)
			                    #print(puntajes)
			                    #print(texto)
			                    #print("asd")
			     
                        except NoSuchElementException:
                            time.sleep(1)#You need to set a "not found value. It's important."
							
			            #Agrego este if por los casos donde concepts no devuelve nada porque son NA
                        if len(puntajes) != 4:
                            puntajes = [-1,-1,-1,-1]
			                #print(puntajes)
							
						#Asigno los valores de puntajes a cada variable segun el orden	
                        comp_and_ben = puntajes[0]
                        cult_and_val = puntajes[1]
                        carrer_op = puntajes[2]
                        work_life_bal = puntajes[3]
									
			
			            #Printing for debugging
                        if verbose:
                            print("Job Title: {}".format(job_title))
                            print("Salary Estimate: {}".format(salary_estimate))
                            print("Job Description: {}".format(job_description[:500]))
                            print("Rating: {}".format(rating))
                            print("Company Name: {}".format(company_name))
                            print("Location: {}".format(location))
			
			            #Going to the Company tab...
			            #clicking on this:
                        time.sleep(1)
                        try:
                            driver.find_element_by_xpath('.//div[@data-item="tab" and @data-tab-type="overview"]').click()
			
                            try:
                                size = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Size"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                size = -1
			
                            try:
                                founded = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Founded"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                founded = -1
			
                            try:
                                type_of_ownership = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Type"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                type_of_ownership = -1
			
                            try:
                                industry = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Industry"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                industry = -1
			
                            try:
                                sector = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Sector"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                sector = -1
			
                            try:
                                revenue = driver.find_element_by_xpath('.//div[span[@class="css-1taruhi e1pvx6aw1"] = "Revenue"]//span[@class="css-i9gxme e1pvx6aw2"]').text
                            except NoSuchElementException:
                                revenue = -1
			
			
                        except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                            size = -1
                            founded = -1
                            type_of_ownership = -1
                            industry = -1
                            sector = -1
                            revenue = -1
			
			                
                        if verbose:
                            print("Size: {}".format(size))
                            print("Founded: {}".format(founded))
                            print("Type of Ownership: {}".format(type_of_ownership))
                            print("Industry: {}".format(industry))
                            print("Sector: {}".format(sector))
                            print("Revenue: {}".format(revenue))
                            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			
                        jobs.append({"Job Title" : job_title,
                        "Salary Estimate" : salary_estimate,
                        "Job Description" : job_description,
                        "Rating" : rating,
                        "Company Name" : company_name,
                        "Location" : location,
                        "Size" : size,
                        "Founded" : founded,
                        "Type of ownership" : type_of_ownership,
                        "Industry" : industry,
                        "Sector" : sector,
                        "Revenue" : revenue,
                        "Compensation_and_Benefits" : comp_and_ben,
                        "Culture_and_Values": cult_and_val,
                        "Career_Opportunities": carrer_op,
                        "Work_Life_Balance": work_life_bal})
			            #add job to jobs
			        
						   
                    df = pd.DataFrame(jobs) #Uncomment to make a dataframe for each page.
                    df.to_csv('Page ' + str(page_num) + '.csv', sep ='\t') #Uncomment to save each page as a CSV.
                    print("Page " + str(page_num) + " scrapped right.")
                    break
                    				
                except:
                    intent = intent + 1  #If it fails, to try again.
                    jobs = jobs[0:((page_num-1)*30)] #Clean the jobs append in the last failed iteration, because it will scrap the same page again
                                       					
        except:			   
             print("You reached the maximum intents number for this page. Scrapping the next one")
			 
    today = date.today().strftime("%d-%b-%Y")
    df = pd.DataFrame(jobs)
    df.to_csv('Glassdoor_Jobs_'+ today + '.csv', sep ='\t')
	
    return df  #This line converts the dictionary object into a pandas DataFrame.