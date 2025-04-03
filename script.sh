python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip3 install --no-cache-dir pyswisseph==2.8.0.post1
pip3 install methodtools==0.4.7
pip3 install scipy==1.15.2
pip3 install astropy==6.1.7
pip3 install sanskrit_data==0.8.14
pip install indic-transliteration
pip3 install curation_utils==0.2.10
pip3 install timebudget==0.7.1
pip install --no-deps jyotisha
#Newly added
pip install "fastapi[standard]"