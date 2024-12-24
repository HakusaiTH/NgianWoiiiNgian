import webbrowser
import base64

class NgianWoiiiNgian:
    def __init__(self):

        self.texts = {
            'thai': """
เงี่ยนโว้ยยย  เงี่ยนนน

เงี่ยนจริงจริง ตายแล้วกู ตายแล้วมั่งเนี่ย

หีอาา หีอมควยตุย หีเป้าขลุ่ยละควยเป่าแตร

หีบอกว่ามันดีแท้ หีเป่าแตรหีอมควยตุ่ย

โอ้ ละมันหีซองการี เมื่อก่อนนี้ทีละบาด 

เดี๋ยวนี้ละมันแพงร้ายกาจร้อยบาทก็ได้ทีเดียว 

โอ้ละมะหีมีเขี้ยวเย็ดทีเดียวกัดควยแทบขาด 

เงี่ยนโว้ยยย เงี่ยนจริงๆ
            """,
            'eng': """
I'm so horny, damn it! Horny!

Really horny, I'm gonna die! I swear I'm dying right now!

Ah, pussy, pussy sucking dick, pussy blowing flute, and dick playing trumpet.

The pussy says it's so damn good, trumpet-blowing pussy sucking dick.

Oh, the pussy Song Ka Ri. Well, of course, it hurt a bit then and it is outrageously expensive 

nowadays-one baht for one round. 

Ah, this pussy has got fangs-one fuck, 

and it bites almost the dick clean off. Damn it, 

I'm so horny! Really horny!
            """,
            'karaoke': """
Ngian Woiii Ngian

Ngian Ching Ching Tai Laeo Ku Tai Laeo Mang Nia

Hi Aaa Hi Om Khuai Tuy Hi Pao Khlui La Khuai Pao Trae

Hi BokWa Man DiThae Hi Pao Trae Hi Om Khuai Tui

OH La Man Hi Song Ka Ri Muea Kon Ni Thila Bat

Diaoni La Man Phaeng Raikat Roi Bat Kodai Thidiao

O La Ma Hi Mi Khiao Yet Thidiao Kat Khuai Thaep Khat

Ngian Woi Ngian Ching Ching
            """
        }

    def NgianWoii_fun(self, eng=False, karaoke=False, open_link=False, count=None, audio=False, count_audio=1):
        if open_link:  
            webbrowser.open("https://youtu.be/cTr69ADnqH0?si=yu_wMThoSXtCaXuU")
        elif count is not None:
            for _ in range(count):
                if eng:
                    print("I'm so horny! Really horny!")
                elif karaoke:
                    print("Ngian Woiii Ngian Ngian Ching Ching")
                else:
                    print("เงี่ยนโว้ยยย  เงี่ยนนน เงี่ยนจริงจริง")
        elif audio:
            try:

                import audio64 

                if count_audio == 1 :
                    base64_audio = audio64.audio_data  

                    final_audio = base64.b64decode(base64_audio)                    
                else :
                    base64_audio = audio64.audio_hor  

                    audio_hor = base64.b64decode(base64_audio)

                    final_audio = audio_hor * count_audio

                with open("output_audio.mp3", "wb") as audio_file:
                    audio_file.write(final_audio)
                print(f"Audio file has been saved as 'output_audio.mp3' with {count_audio} repetitions.")
            except FileNotFoundError:
                print("The file 'audio64.py' was not found.")
            except AttributeError:
                print("The 'audio64.py' file does not contain the expected 'audio_data' variable.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif eng:
            print(self.texts['eng'])
        elif karaoke:
            print(self.texts['karaoke'])
        else:
            print(self.texts['thai'])
