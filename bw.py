import streamlit as st
from datetime import datetime
import time
#import telegram_send
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import asyncio


# get your api_id, api_hash, token
# from telegram as described above
#api_id = os.getenv('API_ID')
#api_hash = os.getenv('API_HASH')
#bot_token = os.getenv('BOT_TOKEN')
api_id = st.secrets['API_ID']
api_hash = st.secrets['API_HASH']
bot_token = st.secrets['BOT_TOKEN']
message = "Connection to Bubble Wand is successful!"
user_id = ''
user_hash = 0
greet_flag = False

 
# your phone number
#phone = os.getenv('BOT_PHONE')

# creating a telegram session and assigning
# it to a variable client


now = datetime.now()

def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )


# To use current hour:
# from datetime import datetime
# part = get_part_of_day(datetime.now().hour)
# print(f"Have a good {part}!")

part = get_part_of_day(int(now.hour))
#st.write(f"hour {now.hour} is {part}")

st.markdown(f'<h1 style="color:#000FFF;font-size:48px;">{"💬Welcome to Bubble Wand!💬"}</h1>', unsafe_allow_html=True)

def main():
    message = "Connection to Bubble Wand is successful!"
    user_id = ''
    send_message = False
    placeholder1 = st.empty()
    placeholder1.header('Hi there ! Tell me about yourself!')
    placeholder2 = st.empty()   
    stu_name = placeholder2.text_input('What is your name?')
    placeholder3 = st.empty()
    stu_class = placeholder3.text_input("What is your teacher's code?")

    if stu_name != '' and stu_class == '':
        
        placeholder1.header(f"Good {part} {stu_name}, wishing you a bubbly day!")
        st.balloons()
        time.sleep(4)
        placeholder1.header(f"Dear {stu_name}, please key in the teacher's code")
        placeholder2.empty()


    if stu_class != '' and stu_class != '':
        placeholder2.empty()
        placeholder3.empty()        
        placeholder1.header(f"Name: {stu_name}")
    
    #st.markdown(f'<h1 style="color:#000FFF;font-size:24px;">{"My Responses"}</h1>', unsafe_allow_html=True)
    #st.markdown('#') 
    placeholder4 = st.empty()
    placeholder4.subheader(f"My Responses:")
    st.markdown('#') 

    happy_emoji = '😃'
    sad_emoji = '😔'
    thumbs_up = '👍'
    thumbs_down = '👎'
    wave = '👋'
    hmmm = '🤔'

    col1, col2 = st.columns(2)
    #col1.button("YES " + thumbs_up)
    if col1.button("YES " + thumbs_up):
        message = f"{stu_name} replied YES " + thumbs_up
        placeholder4.subheader(f"Hey {stu_name}, you answered Yes! 👍 Awesome!")
    col1.markdown('#') 
    if col2.button("NO " + thumbs_down):
        message = f"{stu_name} replied NO " + thumbs_down
        placeholder4.subheader(f"Hey {stu_name}, you answered No! 👎 No problem!")
    col2.markdown('#') 
    if col1.button("HELP ME " + wave):
        message = f"{stu_name} is asking for help! " + wave
        placeholder4.subheader(f"Dear {stu_name}, don't worry, help is coming!")
    col1.markdown('#') 
    if col2.button("DON'T KNOW " + hmmm):
        message = f"{stu_name} does not know " + hmmm
        placeholder4.subheader(f"Dear {stu_name}, don't worry, we will figure it out!")
    col2.markdown('#') 
    if col1.button("CHEERFUL " + happy_emoji):
        message = f"{stu_name} is feeling happy " + happy_emoji
        placeholder4.subheader(f"Hey {stu_name}, I am glad that you are feeling happy! 😃")
    col1.markdown('#') 
    if col2.button("UPSET " + sad_emoji):
        message = f"{stu_name} is feeling sad " + sad_emoji
        placeholder4.subheader(f"Dear {stu_name}, it's ok to feel unhappy, take care")

    st.text(f"Teacher's Code: {stu_class}")    

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    #telegram_send.send(messages=["Wow that was easy!"])
    # connecting and building the session

    client = TelegramClient('bbw_session', api_id, api_hash)

    # async def main():
    #     # Now you can use all client methods listed below, like for example...
    #     async with client.start():
    #         await client.send_message('me', 'Hello to myself!')

    # asyncio.run(main())


    #client = TelegramClient('test_session', api_id, api_hash)
    client.start(bot_token=bot_token)
    #client.connect()

     
    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():
      
        client.send_code_request(stu_class)
         
        # signing in the client
        placeholder5 = st.empty()
        input_code = placeholder5.text_input('Enter the code')
        client.sign_in(stud_class, input_code)
        placeholder5.empty()
      
    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        #receiver = InputPeerUser(user_id, user_hash)
        #print(receiver)
     
        # sending message using telegram client
        print("send_message to user")
        client.send_message(stu_class, message)

    except Exception as e:
         
        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e);
     
    # disconnecting the telegram session
    client.disconnect()



if __name__ == "__main__":
    main()



# st.write("The name is : " + stu_name )
# st.write("The class is : " + stu_class)
