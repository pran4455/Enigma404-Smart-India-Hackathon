from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import AudioRecordingForm
from .models import AudioRecording
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.http import HttpResponse
import base64
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    return render(request, "login.html")

def signup(request):

    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']  # Remember to hash the password before saving

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        # Redirect to login page or any other page you want
        return redirect('login')
    return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                # Successful login
                # You can redirect to the user's dashboard or any other page
                return redirect('dashboard')
            else:
                # Incorrect password
                return render(request, 'login.html', {'error_message': 'Incorrect password'})
        except User.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'error_message': 'User does not exist'})

    return render(request, 'login.html')

def dashboard(request):

    return render(request, 'upload_audio.html')

# @csrf_exempt  # Disable CSRF protection for this view for simplicity; secure it in production.
# def upload_audio(request):
#     if request.method == 'POST':
#         if 'audio_data' in request.FILES:
#             audio_data = request.FILES['audio_data']
#             audio_recording = AudioRecording(audio_data=audio_data)
#             audio_recording.save()
#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'failed', 'error': 'No audio file uploaded'})
#     return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})


def play_audio(request, audio_id):
    try:
        audio_recording = AudioRecording.objects.get(pk=audio_id)
        audio_data = audio_recording.audio_data

        # Serve the audio data as a response with the appropriate content type
        response = HttpResponse(audio_data, content_type='audio/wav')
        response['Content-Disposition'] = 'inline; filename="audio.wav"'
        return response
    except AudioRecording.DoesNotExist:
        return HttpResponseNotFound("Audio recording not found")
    
from django.http import JsonResponse
from .models import AudioRecording

def get_latest_audio_id(request):
    try:
        latest_audio_recording = AudioRecording.objects.latest('created_at')
        latest_audio_id = latest_audio_recording.id
        return JsonResponse({'latest_audio_id': latest_audio_id})
    except AudioRecording.DoesNotExist:
        return JsonResponse({'latest_audio_id': None})
    

# views.py
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import AudioRecording


@csrf_exempt
def record_audio(request):
    if request.method == 'POST':
        try:
            # Access the audio data from request.FILES['audio_data']
            audio_data = request.FILES['audio_data'].read()

            # Save the audio data to your database using your model
            audio_recording = AudioRecording(audio_data=audio_data)
            audio_recording.save()

            # Return a response indicating success
            return JsonResponse({'status': 'success'})
        except Exception as e:
            # Return a response indicating failure and any error message
            return JsonResponse({'status': 'failed', 'error': str(e)})

    return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})

# def play_latest_audio(request):
#     try:
#         latest_audio_recording = AudioRecording.objects.latest('created_at')
#         audio_data = latest_audio_recording.audio_data

#         # Serve the audio data as a response with the appropriate content type
#         response = HttpResponse(audio_data, content_type='audio/wav')
#         response['Content-Disposition'] = 'inline; filename="audio.wav"'
#         return response
#     except AudioRecording.DoesNotExist:
#         return HttpResponseNotFound("Audio recording not found")

def get_latest_audio_id(request):
    try:
        latest_audio_recording = AudioRecording.objects.latest('created_at')
        latest_audio_id = latest_audio_recording.id
        return JsonResponse({'latest_audio_id': latest_audio_id})
    except AudioRecording.DoesNotExist:
        return JsonResponse({'latest_audio_id': None})

from django.http import JsonResponse




# @csrf_exempt
# def upload_audio(request):
#     print("GHJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
#     if request.method == 'POST':
#         if 'audio_data' in request.FILES:
#             audio_data = request.FILES['audio_data'].read()
#             # Encode the audio data in Base64
#             audio_data_base64 = base64.b64encode(audio_data).decode('utf-8')
#             audio_data_dict = {'audio_data': audio_data_base64}

#             json_file_path = '.audio_data.json'
#             with open(json_file_path, 'w') as json_file:
#                 json.dump(audio_data_dict, json_file)

#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'failed', 'error': 'No audio file uploaded'})
#     return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})
import os
from django.http import HttpResponse


# @csrf_exempt  # Disable CSRF protection for simplicity. You should use proper CSRF handling in production.
# def upload_audio(request):
#     if request.method == 'POST':
#         try:
#             print(1)
#             # Get the uploaded audio data from the request
#             audio_data = request.FILES.get('audio_data')
#             print(2)

#             # Define the file path to save the audio as "audio.wav" (you can adjust the path as needed)
#             audio_file_path = os.path.join('D:\Projects\SmartIndiaHackathon\Enigma404\myapp\allaudio', 'audio.wav')
#             print(3)


#             # Save the audio data to the file
#             print(audio_file_path)
#             with open(audio_file_path, 'wb') as audio_file:
#                 print(4)
#                 for chunk in audio_data.chunks():
#                     audio_file.write(chunk)
#             print(4)

#             return HttpResponse(status=204)  # No content response (HTTP 204)
#         except Exception as e:
#             return HttpResponse(status=500)  # Internal Server Error response (HTTP 500)

#     return HttpResponse(status=405)  # Method Not Allowed response (HTTP 405)
import os
from django.http import JsonResponse

import sys
#the correct function
@csrf_exempt
def upload_audio(request):
    if request.method == 'POST':
        try:
            # Get the uploaded audio data from the request
            audio_data = request.FILES.get('audio_data')

            # Define the file path to save the audio as "audio.wav"
            audio_file_path = os.path.join(os.path.dirname(__file__), 'audio.wav')

            # Save the audio data to the file
            print(sys.getsizeof(audio_data))
            with open(audio_file_path, 'wb') as audio_file:
                for chunk in audio_data.chunks():
                    print(1)
                    audio_file.write(chunk)

            return JsonResponse({'message': 'Audio successfully uploaded.'})
        except Exception as e:
            logger.error('Error while processing audio upload: %s', str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

from django.http import JsonResponse, HttpResponse
from django.http import FileResponse
import io
from django.http import HttpResponse, JsonResponse
import logging

@csrf_exempt
def play_latest_audio(request):
    if request.method == 'GET':
        try:
            # Read audio data from the JSON file
            with open('audio_data.json', 'r') as json_file:
                audio_data_dict = json.load(json_file)

            # Extract the audio data
            audio_data_base64 = audio_data_dict.get('audio_data', '')

            # Decode the base64 audio data
            audio_data_bytes = base64.b64decode(audio_data_base64)

            # Convert the binary audio data to an AudioSegment (assuming it's in MP3 format)
            audio = AudioSegment.from_file(io.BytesIO(audio_data_bytes), format="mp3")

            # Export the AudioSegment as a WAV file with good quality settings
            wav_data = audio.set_channels(1).set_sample_width(2).set_frame_rate(44100).raw_data

            # Set the response content type to audio/wav
            response = HttpResponse(wav_data, content_type='audio/wav')
            response['Content-Disposition'] = 'attachment; filename="audio.wav"'

            return response
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Method Not Allowed'}, status=405)



def play_latest_audio_page(request):
    return render(request, 'testing.html')


from django.http import HttpResponse, JsonResponse


@csrf_exempt
def get_audio_data(request):
    if request.method == 'GET':
        try:
            # Load the JSON data from the JSON file
            with open('.audio_data.json', 'r') as json_file:
                audio_data_dict = json.load(json_file)

            # Extract the audio data as a base64-encoded string
            audio_data_base64 = audio_data_dict.get('audio_data', '')

            if audio_data_base64:
                # Decode the base64 audio data to binary
                audio_binary = base64.b64decode(audio_data_base64)

                # Return the audio data as a binary response
                response = HttpResponse(audio_binary, content_type='audio/wav')
                response['Content-Disposition'] = 'inline; filename="audio.wav"'
                return response
            else:
                return JsonResponse({'error': 'No audio data found in JSON.'})

        except FileNotFoundError:
            print("JSON file not found")
            return JsonResponse({'error': 'No audio data found.'})

    return JsonResponse({'error': 'Invalid request method.'})













import pyaudio
import wave
from django.shortcuts import render, redirect
from .forms import AudioRecordingForm

def capture_and_save_audio(request):
    if request.method == 'POST':
        form = AudioRecordingForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio_file = request.FILES['audio_file']
            audio.audio_file = 'audio_recordings/' + audio_file.name
            
            # Capture live audio and save it as a .wav file
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            frames = []
            for _ in range(0, int(44100 / 1024 * 5)):  # Capture audio for 5 seconds
                data = stream.read(1024)
                frames.append(data)
            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(audio.audio_file.path, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            audio.save()
            return redirect('audio_list')  # Redirect to a view that lists audio recordings
    else:
        form = AudioRecordingForm()
    return render(request, 'capture_audio.html', {'form': form})
