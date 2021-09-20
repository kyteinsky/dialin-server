from twilio.twiml.voice_response import Conference, Dial, VoiceResponse

def joinRoom(roomName):
    response = VoiceResponse()
    dial = Dial()
    dial.conference(roomName)
    response.append(dial)

    print(response)

