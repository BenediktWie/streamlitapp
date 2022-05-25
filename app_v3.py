### Overall setup###

import streamlit as st
import pandas as pd
import pickle 
#import statsmodels.api as sm
#import numpy as np
#import xgboost 

### Defining some general properties of the app  
st.set_page_config(
    page_title= "HeartDrive",
    page_icon='💓',
    layout='wide' )


###Title, picture and App description
st.title("💓 HeartDrive - Heart Disease Prediction with Lifestyle-Change Recommendations 💓")

from PIL import Image
image = Image.open('healthcare.jpg')
st.image(image, use_column_width='always', caption='')

st.markdown("Do you know the world's number one cause of death? According to the WHO, heart diseases are responsible for 16% of the world's total deaths.")
st.markdown("This application aims to reduce this phenomenon by improving the identification of heart diseases, in this case especially heart attacks. By using an ensemble of Maschine Learning Models based on a Dataset from the Centre for Disease Control and Prevention (CDC), the individual probability for a heart attack will be predicted. This may raise awareness about the personal lifestyle and therefore reduce the risk of an heart attack.")

###The following section defines the Variables used for the prediction. For improved customer usability, 
### it will be distinguished between Life Situational Data and Medical Data.
st.sidebar.header("1 Personal Data 👩🧑")
st.sidebar.subheader("1.1 Life Situational Data 🍷⚽")
st.sidebar.info('ℹ️  These variables refer to your current personal lifesituation. Please answer them as precisely as possible!')



#MAXDRNKS   
option11 = st.sidebar.number_input("During the past 30 days, what is the largest number of drinks you had on any occasion? (77 for Don't know / 99 for Refuse to answer)", min_value=0, max_value=99, value=0)   
if option11 in range(78,99):
   st.sidebar.error('Please only choose values that fulfill the criteria above! The maximum is 76 drink occasions.') 

#USENOW3         
option12 = st.sidebar.selectbox(
 'Do you currently use chewing tobacco, snuff, or snus every day, some days, or not at all?',
 ('Every day', 'Some days', "Not at all",
  "Don't know", 'Refuse to answer'))

if option12  == 'Every day':
    option12 = 1
elif option12 == 'Some days':
    option12 = 2
elif option12 == "Not at all":
    option12 = 3
elif option12 == "Don't know":
    option12 = 7
elif option12 == 'Refuse to answer':
    option12 = 9
    
#PREGNANT    
option13 = st.sidebar.selectbox(
 'To your knowledge, are you now pregnant?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))

if option13 == 'Yes':
    option13 = 1
elif option13 == 'No':
    option13 = 2
elif option13 == "Don't know":
    option13 = 7
elif option13 =='Refuse to answer':
    option13 = 9
    
  

#CPDEMO1B
option21 = st.sidebar.selectbox(
 'How many cell phones do you have for personal use?',
 (1,2,3,4,5, '6 or more', "Don't know", 'None', 'Refuse to answer'))


if option21  == '6 or more':
    option21 = 6
elif option21 == "Don't know":
    option21 = 7
elif option21 == 'None':
    option21 = 8
elif option21 == 'Refuse to answer':
    option21 = 9
    
    
#LCSLAST
option22 = st.sidebar.number_input("How old were you when you last smoked cigarettes regularly? (777 for Don't know / 999 for Refuse to answer", min_value=0, max_value=999, value=0)
if option22 in range(100,777):
   st.sidebar.error('Please only choose values that fulfill the criteria above! The maximum years is 100.') 
elif option22 in  range(778,999):
   st.sidebar.error('Please only choose values that fulfill the criteria above! The maximum years is 100.')

#FEETCHK
option23 = st.sidebar.number_input(
 "About how many times in the past 12 months has a health professional checked your feet for any sores or irritations? (77 for Don't know / 88 for None/ 99 for Refuse to answer", min_value=1, max_value=99, value=1)
if option23 in range(78,88):
   st.sidebar.error('Please only choose values that fulfill the criteria above! The maximum is 76 feet checks.')     
if option23 in range(89,99):
   st.sidebar.error('Please only choose values that fulfill the criteria above! The maximum is 76 feet checks.')     

 #EXERANY2
option31 = st.sidebar.selectbox(
 'During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise? ',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))
 

if option31 == 'Yes':
    option31 = 1
elif option31 == 'No':
    option31 = 2
elif option31 == "Don't know":
    option31 = 7
elif option31 =='Refuse to answer':
    option31 = 9
     
#MEDCOST
option32 = st.sidebar.selectbox(
 'Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option32 == 'Yes':
    option32 = 1
elif option32 == 'No':
    option32 = 2
elif option32 == "Don't know":
    option32 = 7
elif option32 =='Refuse to answer':
    option32 = 9

#DRNKANY5
option33 = st.sidebar.selectbox(
 'Did you have at least one drink of alcohol in the past 30 days?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option33 == 'Yes':
    option33 = 1
elif option33 == 'No':
    option33 = 2
elif option33 == "Don't know":
    option33 = 7
elif option33 =='Refuse to answer':
    option33 = 9
    
#CHECKUP1
option34 = st.sidebar.selectbox(
 'About how long has it been since you last visited a doctor for a routine checkup?',
 ('Within past year', 'Within past 2 years', "Within past 5 years",
  '5 or more years ago', 'Don’t know/Not sure ', 'Never', 'Refuse to answer'))
   

if option34  == 'Within past year':
    option34 = 1
elif option34 == 'Within past 2 years':
    option34 = 2
elif option34 == "Within past 5 years":
    option34 = 3
elif option34 == '5 or more years ago':
    option34 = 4
elif option34 == 'Don’t know/Not sure ':
    option34 = 7
elif option34 == 'Never':
    option34 = 8
elif option34 == 'Refuse to answer':
    option34 = 9
    
#HIVRISK5
option35 = st.sidebar.selectbox(
 'Does any of the following situations apply to you? You have injected any drug other than those prescribed for you in the past year. You have been treated for a sexually transmitted disease or STD in the past year. You have given or received money or drugs in exchange for sex in the past year.',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option35 == 'Yes':
    option35 = 1
elif option35 == 'No':
    option35 = 2
elif option35 == "Don't know":
    option35 = 7
elif option35 =='Refuse to answer':
    option35 = 9
        
#VETERAN3
option36 = st.sidebar.selectbox(
 'Have you ever served on active duty in the United States Armed Forces, either in the regular military or in a National Guard or military reserve unit?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option36 == 'Yes':
    option36 = 1
elif option36 == 'No':
    option36 = 2
elif option36 == "Don't know":
    option36 = 7
elif option36 =='Refuse to answer':
    option36 = 9
    
#EMPLOY1        
option37 = st.sidebar.selectbox(
 'Are you currently ...?',
 ('Employed for wages', 'Self-employed', "Out of work for 1 year or more",
  'Out of work for less than 1 year', 'A homemaker', 'A student', 'Retired', 'Unable to work', 'Refuse to answer'))
   

if option37  == 'Employed for wages':
    option37 = 1
elif option37 == 'Self-employed':
    option37 = 2
elif option37 == "Out of work for 1 year or more":
    option37 = 3
elif option37 == 'Out of work for less than 1 year':
    option37 = 4
elif option37 == 'A homemaker':
    option37 = 5
elif option37 == 'A student':
    option37 = 6
elif option37 == 'Retired':
    option37 = 7
elif option37 == 'Unable to work':
    option37 = 8
elif option37 == 'Refuse to answer':
    option37 = 9
    
st.sidebar.subheader("1.2 Personal Medical Data ⚕️🏥")
st.sidebar.info('ℹ️   These variables refer to your medical record. Please answer them as precisely as possible!')
    
    
    
#GENHLTH
option41 = st.sidebar.selectbox(
 'Would you say that in general your health is',
 ('Excellent', 'Very good', 'Good', 'Fair', 'Poor', "Don't know", 'Refuse to answer'))
 
     
if option41  == 'Excellent':
    option41 = 1
elif option41 == 'Very good':
    option41 = 2
elif option41 == "Good":
    option41 = 3
elif option41 == 'Fair':
    option41 = 4
elif option41 == 'Poor':
    option41 = 5
elif option41 == "Don't know":
    option41 = 7
elif option41 == 'Refuse to answer':
    option41 = 9
    
#PDIABTST
option42 = st.sidebar.selectbox(
 'Have you had a test for high blood sugar or diabetes within the past three years?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option42 == 'Yes':
    option42 = 1
elif option42 == 'No':
    option42 = 2
elif option42 == "Don't know":
    option42 = 7
elif option42 =='Refuse to answer':
    option42 = 9

 #RMVTETH4
option43 = st.sidebar.selectbox(
 'Not including teeth lost for injury or orthodontics, how many of your permanent teeth have been removed because of tooth decay or gum disease?',
 ('1 to 5', '6 or more, but not all', 'All', "Don't know", 'None', 'Refuse to answer'))


if option43 == '1 to 5':
    option43 = 1
elif option43 == '6 or more, but not all':
    option43 = 2
elif option43 == 'All':
    option43 = 3
elif option43 == 'None':
    option43 = 8    
elif option43 == "Don't know":
    option43 = 7
elif option43 =='Refuse to answer':
    option43 = 9


#BLDSUGAR
option51 = st.sidebar.number_input("About how often do you check your blood for glucose or sugar? [Include times when checked by a family member or friend, but do NOT include times when checked by a health professional.] (101-199 for _ _ times for day, 201-299 for _ _ times per week, 301-399 for _ _ times per month, 401-499 for _ _ times per year, 777 for Don't know / 888 for None / 999 for Refuse to answer)", min_value=1, max_value=999, value=1)



 #CHCKDNY2
option52 = st.sidebar.selectbox(
 'Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))
   

if option52 == 'Yes':
    option52 = 1
elif option52 == 'No':
    option52 = 2
elif option52 == "Don't know":
    option52 = 7
elif option52 =='Refuse to answer':
    option52 = 9

 #CVDCRHD4
option53 = st.sidebar.selectbox(
 'Ever told you had angina or coronary heart disease?',
 ('Yes', "No / Don't know / Refuse to answer"))


if option53 == 'Yes':
    option53 = 1
elif option53 == "No / Don't know / Refuse to answer":
    option53 = 2
  
  


 #CHCOCNCR
option63 = st.sidebar.selectbox(
 'Ever told you had any other types of cancer?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option63 == 'Yes':
    option63 = 1
elif option63 == 'No':
    option63 = 2
elif option63 == "Don't know":
    option63 = 7
elif option63 =='Refuse to answer':
    option63 = 9

    


#CVDSTRK3
option71 = st.sidebar.selectbox(
 '(Ever told) (you had) a stroke?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))
  
     
if option71 == 'Yes':
    option71 = 1
elif option71 == 'No':
    option71 = 2
elif option71 == "Don't know":
    option71 = 7
elif option71 =='Refuse to answer':
    option71 = 9

#PHYSHLTH
option72 = st.sidebar.selectbox(
 'Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?',
 (1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 
  'None', "Don't know", 'Refuse to answer')) 


if option72 == 'None':
    option72 = 88
elif option72 == "Don't know":
    option72 = 77
elif option72 =='Refuse to answer':
    option72 = 99


 #HLTHPLN1
option73 = st.sidebar.selectbox(
 'Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare, or Indian Health Service?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))
   

if option73 == 'Yes':
    option73 = 1
elif option73 == 'No':
    option73 = 2
elif option73 == "Don't know":
    option73 = 7
elif option73 =='Refuse to answer':
    option73 = 9
             
 #ASTHMA3
option74 = st.sidebar.selectbox(
 'Ever told you had asthma?',
 ('Yes', 'No', "Don't know", 'Refuse to answer'))


if option74 == 'Yes':
    option74 = 1
elif option74 == 'No':
    option74 = 2
elif option74 == "Don't know":
    option74 = 7
elif option74 =='Refuse to answer':
    option74 = 9
            



#In the next step, we create a Dataframe which will be used for the prediction.

df_user = pd.DataFrame(columns= [
 'GENHLTH',
 'CHCOCNCR',
 'USENOW3',
 'PREGNANT',
 'PHYSHLTH',
 'FEETCHK',
 'EMPLOY1',
 'VETERAN3',
 'CPDEMO1B',
 'LCSLAST',
 'RMVTETH4',
 'MAXDRNKS',
 'DRNKANY5',
 'CHCKDNY2',
 'CHECKUP1',
 'ASTHMA3',
 'CVDSTRK3',
 'CVDCRHD4',
 'PDIABTST',
 'HLTHPLN1',
 'BLDSUGAR',
 'HIVRISK5',
 'MEDCOST',
 'EXERANY2'])

df_user.loc[0] = [option41,option63,option12,option13,option72,option23,option37,option36,option21,
             option22,option43,option11,option33,option52,option34,option74,option71,option53,option42,
             option73,option51,option35,option32,option31]
df_user = df_user.astype(float)

#In the following, we load our trained model and predict the probability with the given input data. 

st.header("Personal Predicted Probability 🔍")
st.info('ℹ️   Please be aware that this prediction is preliminary and cannot replace a professional diagnosis!')
#if st.button('Predict now!'):
loaded_model = pickle.load(open('voting.sav', 'rb'))
prediction = loaded_model.predict_proba(df_user)
#percentage = "{:.3%}".format(prediction) 
prediction = prediction[0,1]
percentage = "{:.3%}".format(prediction)

if prediction > 0.5:
    image2 = Image.open('herz.jpg')
    st.image(image2)
    st.metric(label="Probability", value= percentage)
    st.error("You have a high heart attack risk! Check how lifestyle changes could improve your risk status in the section below!")

if prediction <= 0.5 and prediction > 0.01:
   image4 = Image.open('Herz2.jpg')
   st.image(image4)
   st.metric(label="Probability", value= percentage)
   st.warning("Your heart attack risk is not negligible! Check how lifestyle changes could improve your risk status in the section below!")

if prediction <= 0.01:
    image3 = Image.open('glück.jpg')
    st.image(image3, width = None)
    st.metric(label="Probability", value= percentage)
    st.success("Your personal heart attack risk is low! Keep on your lifestyle and stay healthy! \n \n Futhermore, check how  lifestyle changes could further improve your risk status in the section below!")

#For Lifestyle Recommendations, we redefine Variables, which are lifestyle related and can therefore be changed.
#We set the relevant variables to values, which we derived from scienfic papers. 

st.header("Lifestyle Recommendations 🚀")
if st.button('Change current lifestyle and reduce heart attack risk!'):
    option35_improved = 2 
    option34_improved = 1
    option31_improved = 1
    option23_improved = 76
    option22_improved = 0
    option12_improved = 3

    df_user1 = pd.DataFrame(columns= [
     'GENHLTH',
     'CHCOCNCR',
     'USENOW3',
     'PREGNANT',
     'PHYSHLTH',
     'FEETCHK',
     'EMPLOY1',
     'VETERAN3',
     'CPDEMO1B',
     'LCSLAST',
     'RMVTETH4',
     'MAXDRNKS',
     'DRNKANY5',
     'CHCKDNY2',
     'CHECKUP1',
     'ASTHMA3',
     'CVDSTRK3',
     'CVDCRHD4',
     'PDIABTST',
     'HLTHPLN1',
     'BLDSUGAR',
     'HIVRISK5',
     'MEDCOST',
     'EXERANY2'])

    df_user1.loc[0] = [option41,option63,option12_improved,option13,option72,option23_improved,option37,option36,option21,
                 option22_improved,option43,option11,option33,option52,option34_improved,option74,option71,option53,option42,
                 option73,option51,option35_improved,option32,option31_improved]
    df_user1 = df_user1.astype(float)
    loaded_model = pickle.load(open('voting.sav', 'rb'))
    
    prediction2 = loaded_model.predict_proba(df_user1)
    #percentage = "{:.3%}".format(prediction[0]) 
    prediction2 = prediction2[0,1]
    percentage2 = "{:.3%}".format(prediction2)
    
    if prediction2 > prediction:
        st.info("There are no available lifestyle improvements to your personal risk status! Please consult your personal doctor for further health care measures!")
    else:   
        image2 = Image.open('Ruhe.jpg')
        st.image(image2)
            
        st.metric(label="Probability", value = percentage2)
        st.write("Here are some recommendations for your personal live which can help to reduce your heart attack probability!")
        
        
        if option35_improved != option35:
            st.success("According to a study by Hsue and Walters (2018), individuals with HIV have a significantly higher risk for heart attacks. Please make sure to stop engaging in activities with high HIV risks.🦠💉")
        if option34_improved != option34: 
            st.success("Getting a regular routine checkup at your personal doctor may also improve your personal heart attack risk. This was explored in a study by Alageel & Gulliford, conducted in collaboration with the NHS in the UK (2019).🏥🧑‍⚕️")
        if option31_improved != option31:
            st.success("Even short exercises every day can decrease your personal heart attack risk. Find yourself an fitting physical activity, your heart will thank it to you!🧗🏌️")
        if option23_improved != option23: 
            st.success("Even if it seems surprising, there is a connection between foot pain and heart attacks since foot pain is a common symptom for heart diseases. Make sure to check you feet! 🦶🔍")
        if option22_improved != option22:
            st.success("Smoking increases the formation of plaque in blood bessels. Therefore, your blood vessels become more narrow, which increases your personal risk for a heart attack. Stop smoking! 🚬🫁")
        if option12_improved != option12:
            st.success("Even if it presents itself as an alternative to smoking, the use of snus (and similar) still increases plaque in your blood vessels and increases your heart attack risk. Find youself a different habit! 🛑☠️")
        
 
       