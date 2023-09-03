import streamlit as st
import numpy as np
import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import hashlib
from mydatabase import *
matplotlib.use("Agg")
st.set_option('deprecation.showPyplotGlobalUse', False)

best_features=['protime', 'sgot', 'bilirubin', 'age', 'alk_phosphate', 'albumin',
    'spiders', 'histology', 'malaise', 'fatigue', 'ascites', 'varices']

gender_dict={"male":1,"female":2}
feature_dict={"No":1,"Yes":2}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value

def get_key(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return key
def load_model(model_file):
    loaded_model=joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model
        
def get_fvalue(val):
    feature_dict={"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val==key:
            return value

def generate_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def verify_hash(password,hashedpassword):
    if generate_hash(password)==hashedpassword:
        return hashedpassword
    return False


def load_image(img):
	im =Image.open(os.path.join(img))
	return im
	

def change_avatar(sex):
	if sex == "male":
		avatar_img = 'img_avatar.png'
	else:
		avatar_img = 'img_avatar2.png'
	return avatar_img
html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Disease Mortality Prediction </h1>
		<h5 style="color:white;text-align:center;">Hepatitis B </h5>
		</div>
		"""

# Avatar Image using a url
avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"

result_temp ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
        <h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
        <br/>
        <br/>	
        <p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
        </div>
        """

result_temp2 ="""
        <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
        <h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
        <img src="https://www.w3schools.com/howto/{}" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
        <br/>
        <br/>	
        <p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
        </div>
        """

prescriptive_message_temp ="""
        <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
            <h3 style="text-align:justify;color:black;padding:10px">Recommended Life style modification</h3>
            <ul>
            <li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
            <li style="text-align:justify;color:black;padding:10px">Get Plenty of Rest</li>
            <li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
            <li style="text-align:justify;color:black;padding:10px">Avoid Alchol</li>
            <li style="text-align:justify;color:black;padding:10px">Proper diet</li>
            <ul>
            <h3 style="text-align:justify;color:black;padding:10px">Medical Mgmt</h3>
            <ul>
            <li style="text-align:justify;color:black;padding:10px">Consult your doctor</li>
            <li style="text-align:justify;color:black;padding:10px">Take your interferons</li>
            <li style="text-align:justify;color:black;padding:10px">Go for checkups</li>
            <ul>
        </div>
        """


descriptive_message_temp ="""
        <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
            <h3 style="text-align:justify;color:black;padding:10px">Definition</h3>
            <p>Hepatitis B is a viral infection that attacks the liver and can cause both acute and chronic disease.</p>
        </div>
        """
        
        

def main():
    st.title("Disease mortality Prediction App")
    menu=["Home", "Login","Signup"]
    submenu=["Plot", "Prediction"]
    
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Home":
        st.subheader("Home")
        st.text("what is hepatitis?")
        
        st.markdown(descriptive_message_temp,unsafe_allow_html=True)
		# st.image(load_image('images/hepimage.jpeg'))
    
    elif choice=="Login":
        username=st.sidebar.text_input("username")
        password=st.sidebar.text_input("password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd=generate_hash(password)
            # if password=="12345":
            result=login_user(username,verify_hash(password,hashed_pswd))
            if result:
                st.success("Welcome {}".format(username))
                activity=st.selectbox("Activity",submenu)
                if activity=="Plot":
                    st.subheader("Data vis Plot")
                    df=pd.read_csv("cleaned.csv").reset_index()
                    df=df.drop("Unnamed: 0",axis=1)
                    df=df.drop("index",axis=1)
                    st.dataframe(df)
                    
                    df["class"].value_counts().plot(kind="barh")
                    st.pyplot()
                    freqdf=pd.read_csv("freq_df_hepatitis_dataset.csv")
                    st.bar_chart(freqdf["count"])
                    
                    
                    if st.checkbox("Area chart"):
                        clean_columns=df.columns.to_list()
                        feat_choices=st.multiselect("Choose features",clean_columns)
                        new_df=df[feat_choices]
                        st.area_chart(new_df)
                        


# best_features=['protime', 'sgot', 'bilirubin', 'age', 'alk_phosphate', 'albumin',
#     'spiders', 'histology', 'malaise', 'fatigue', 'ascites', 'varices']

                elif activity=="Prediction":
                    st.subheader("Predictive analysis")
                    age=st.number_input("age",7,80)
                    protime=st.number_input("protime",0.0,100.0)
                    sgot=st.number_input("sgot",0.0,700.0)
                    bilirubin=st.number_input("bilirubin",0.0,8.0)
                    alk_phosphate=st.number_input("alk_phosphate",0.0,300.0)
                    albumin=st.number_input("albumin",0.0,8.0)
                    sex=st.radio("Sex",tuple(gender_dict.keys()))
                    spiders=st.radio("spider?",tuple(feature_dict.keys()))
                    steroid=st.radio("DO you take Steroid?",tuple(feature_dict.keys()))
                    antivirals=st.radio("DO you take antivirals?",tuple(feature_dict.keys()))
                    histology=st.radio("DO you have histology?",tuple(feature_dict.keys()))
                    malaise=st.radio("DO you have malaise?",tuple(feature_dict.keys()))
                    fatigue=st.radio("DO you have fatigue?",tuple(feature_dict.keys()))
                    ascites=st.radio("DO you have ascites?",tuple(feature_dict.keys()))
                    varices=st.radio("DO you have varices?",tuple(feature_dict.keys()))
                    anorexia=st.radio("DO you have anorexia?",tuple(feature_dict.keys()))
                    liver_big=st.radio("DO you have liver_big?",tuple(feature_dict.keys()))
                    liver_firm=st.radio("DO you have liver_firm?",tuple(feature_dict.keys()))
                    spleen_palpable=st.radio("DO you have spleen_palpable?",tuple(feature_dict.keys()))
                    
                    pretty_result = {'age':age, 'sex':sex, 'steroid':steroid, 'antivirals':antivirals, 'fatigue':fatigue, 'malaise':malaise, 'anorexia':anorexia,
    'liver_big':liver_big, 'liver_firm':liver_firm, 'spleen_palpable':spleen_palpable, 'spiders':spiders, 'ascites':ascites,
    'varices':varices, 'bilirubin':bilirubin, 'alk_phosphate':alk_phosphate, 'sgot':sgot, 'albumin':albumin, 'protime':protime,
    'histology':histology}
                    st.json(pretty_result)
                    
                    
                    feature_list=[age,get_value(sex,gender_dict),get_fvalue(steroid),get_fvalue(antivirals),get_fvalue(fatigue),get_fvalue(malaise),get_fvalue(anorexia),get_fvalue(liver_big),get_fvalue(liver_firm),get_fvalue(spleen_palpable),get_fvalue(spiders),get_fvalue(ascites),get_fvalue(varices),bilirubin,alk_phosphate,sgot,albumin,protime,get_fvalue(histology)]
                    sample_data=np.array(feature_list).reshape(1,-1)
                    
                    
                    model_choice=st.selectbox("Select model",["Decision Tree","GradientBoost","Random Forest"])
                    if st.button("predict"):
                        if model_choice=="Decision Tree":
                            loader_model=load_model("dt_model.pkl")
                            p=loader_model.predict(sample_data)
                            pred_prob=loader_model.predict_proba(sample_data)
                           
                        elif model_choice=="GradientBoost":
                            loader_model=load_model("gb_model.pkl")
                            p=loader_model.predict(sample_data)
                            pred_prob=loader_model.predict_proba(sample_data)
                       
                        elif model_choice=="Random Forest":
                            loader_model=load_model("random_forest_model.pkl")
                            p=loader_model.predict(sample_data)
                            pred_prob=loader_model.predict_proba(sample_data)
                        st.write(p)
                      
                        if p==1:
                            st.warning("Danger")
                        else:
                            st.success("Safe")
                            pred_score={"Danger":pred_prob[0][0]*100,"Safe":pred_prob[0][1]*100}
                            st.subheader("Prediction Probabilistic Score using {}".format(model_choice))
                            st.json(pred_score)
                    
                    
            else:
                st.warning("incorrect username or password")
                
    elif choice == "Signup":
        new_user=st.text_input("username")
        new_password=st.text_input("password",type="password")
        confirm_password=st.text_input("Confirm Password",type="password")
        if new_password==confirm_password:
            st.success("Password confirmed")
        else:
            st.warning("Invalid password")
        if st.button("submit"):
            create_usertable()
            hashed_new_password=generate_hash(new_password)
            
            add_userdata(new_user,hashed_new_password)
            st.success("you have successfully signed up")
            st.info("login now")
                    
if __name__ == "__main__":
    main()