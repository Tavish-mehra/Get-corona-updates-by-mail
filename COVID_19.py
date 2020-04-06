import requests
import smtplib
import pandas as pd
# from datetime import datetime
# from threading import Timer

# def corona_update():
df = pd.read_html(requests.get('https://www.worldometers.info/coronavirus/').content)[-1]
df.set_index("Country,Other", inplace=True)
India = df.loc['India']
data = India.to_list()

total_cases = data[0]
new_cases = data[1]
total_deaths = data[2]
active_cases = data[5]
total_recovered = data[4]

server = smtplib.SMTP('smtp.gmail.com', 25, 'localhost')
server.ehlo()
server.starttls()
server.ehlo()
server.login('email', 'password')
subject = 'Coronavirus stats in your country today!'
body = 'Today in India'  + '\
\nThere is new data on coronavirus:\
\nTotal cases: ' + str(total_cases) +'\
\nNew cases: ' + str(new_cases) + '\
\nTotal deaths: '+  str(total_deaths) + '\
\nActive cases: ' + str(active_cases) + '\
\nTotal recovered: ' + str(total_recovered) + '\
\nCheck the link: https://www.worldometers.info/coronavirus/'
message = f"Subject: {subject}\n\n{body}"
# print(message)
server.sendmail('Coronavirus','email',message)
print('Hey Email has been sent!')
server.quit()

# x=datetime.today()
# y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
# delta_t=y-x

# secs=delta_t.seconds+1


# t = Timer(secs,corona_update)
# t.start()



