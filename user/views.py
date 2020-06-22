import os, shutil
from DB import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import user, details, folder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
import random

STORAGE = (settings.BASE_DIR).replace('\\', '/')

mime = {
    'js': 'application/javascript',
    'mjs': 'application/javascript',
    'json': 'application/json',
    'webmanifest': 'application/manifest+json',
    'doc': 'application/msword',
    'dot': 'application/msword',
    'wiz': 'application/msword',
    'bin': 'application/octet-stream',
    'a': 'application/octet-stream',
    'dll': 'application/octet-stream',
    'exe': 'application/octet-stream',
    'o': 'application/octet-stream',
    'obj': 'application/octet-stream',
    'so': 'application/octet-stream',
    'oda': 'application/oda',
    'pdf': 'application/pdf',
    'p7c': 'application/pkcs7-mime',
    'ps': 'application/postscript',
    'ai': 'application/postscript',
    'eps': 'application/postscript',
    'm3u': 'application/vnd.apple.mpegurl',
    'm3u8': 'application/vnd.apple.mpegurl',
    'xls': 'application/vnd.ms-excel',
    'xlb': 'application/vnd.ms-excel',
    'ppt': 'application/vnd.ms-powerpoint',
    'pot': 'application/vnd.ms-powerpoint',
    'ppa': 'application/vnd.ms-powerpoint',
    'pps': 'application/vnd.ms-powerpoint',
    'pwz': 'application/vnd.ms-powerpoint',
    'wasm': 'application/wasm',
    'bcpio': 'application/x-bcpio',
    'cpio': 'application/x-cpio',
    'csh': 'application/x-csh',
    'dvi': 'application/x-dvi',
    'gtar': 'application/x-gtar',
    'hdf': 'application/x-hdf',
    'latex': 'application/x-latex',
    'mif': 'application/x-mif',
    'cdf': 'application/x-netcdf',
    'nc': 'application/x-netcdf',
    'p12': 'application/x-pkcs12',
    'pfx': 'application/x-pkcs12',
    'ram': 'application/x-pn-realaudio',
    'pyc': 'application/x-python-code',
    'pyo': 'application/x-python-code',
    'sh': 'application/x-sh',
    'shar': 'application/x-shar',
    'swf': 'application/x-shockwave-flash',
    'sv4cpio': 'application/x-sv4cpio',
    'sv4crc': 'application/x-sv4crc',
    'tar': 'application/x-tar',
    'tcl': 'application/x-tcl',
    'tex': 'application/x-tex',
    'texi': 'application/x-texinfo',
    'texinfo': 'application/x-texinfo',
    'roff': 'application/x-troff',
    't': 'application/x-troff',
    'tr': 'application/x-troff',
    'man': 'application/x-troff-man',
    'me': 'application/x-troff-me',
    'ms': 'application/x-troff-ms',
    'ustar': 'application/x-ustar',
    'src': 'application/x-wais-source',
    'xsl': 'application/xml',
    'rdf': 'application/xml',
    'wsdl': 'application/xml',
    'xpdl': 'application/xml',
    'zip': 'application/zip',
    'au': 'audio/basic',
    'snd': 'audio/basic',
    'mp3': 'audio/mpeg',
    'mp2': 'audio/mpeg',
    'aif': 'audio/x-aiff',
    'aifc': 'audio/x-aiff',
    'aiff': 'audio/x-aiff',
    'ra': 'audio/x-pn-realaudio',
    'wav': 'audio/x-wav',
    'bmp': 'image/bmp',
    'gif': 'image/gif',
    'ief': 'image/ief',
    'jpg': 'image/jpeg',
    'jpe': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'tiff': 'image/tiff',
    'tif': 'image/tiff',
    'ico': 'image/vnd.microsoft.icon',
    'ras': 'image/x-cmu-raster',
    'bmp': 'image/x-ms-bmp',
    'pnm': 'image/x-portable-anymap',
    'pbm': 'image/x-portable-bitmap',
    'pgm': 'image/x-portable-graymap',
    'ppm': 'image/x-portable-pixmap',
    'rgb': 'image/x-rgb',
    'xbm': 'image/x-xbitmap',
    'xpm': 'image/x-xpixmap',
    'xwd': 'image/x-xwindowdump',
    'eml': 'message/rfc822',
    'mht': 'message/rfc822',
    'mhtml': 'message/rfc822',
    'nws': 'message/rfc822',
    'css': 'text/css',
    'csv': 'text/csv',
    'html': 'text/html',
    'htm': 'text/html',
    'txt': 'text/plain',
    'bat': 'text/plain',
    'c': 'text/plain',
    'h': 'text/plain',
    'ksh': 'text/plain',
    'pl': 'text/plain',
    'rtx': 'text/richtext',
    'tsv': 'text/tab-separated-values',
    'py': 'text/x-python',
    'etx': 'text/x-setext',
    'sgm': 'text/x-sgml',
    'sgml': 'text/x-sgml',
    'vcf': 'text/x-vcard',
    'xml': 'text/xml',
    'mp4': 'video/mp4',
    'mpeg': 'video/mpeg',
    'm1v': 'video/mpeg',
    'mpa': 'video/mpeg',
    'mpe': 'video/mpeg',
    'mpg': 'video/mpeg',
    'mov': 'video/quicktime',
    'qt': 'video/quicktime',
    'webm': 'video/webm',
    'avi': 'video/x-msvideo',
    'movie': 'video/x-sgi-movie',
}


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        valid = authenticate(username=username, password=password)
        if valid is not None:
            login(request, valid)
            request.session['cdir'] = STORAGE + '/' + username
            return redirect('/user/index/')
        else:
            return render(request, 'login.html', context={"messages": 'Incorrect username/password'})

    else:
        return render(request, 'login.html')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        email = request.POST['email']
        bdate = request.POST['bdate']
        mono = request.POST['mono']
        fname = STORAGE + '/' + username
        if password == cpassword and authenticate(username=username) is None:
            os.mkdir(fname)
            f = folder(user_id=username, fname=fname)
            user_details = details(username_id=username, password=password, gender=gender, email=email, bdate=bdate,
                                   mono=mono)
            users = user(user_id=username, password=password)
            users.save()
            user_details.save()
            f.save()
            auth_user = User.objects.create_user(username, email, password)
            auth_user.save()
            return redirect('/user/index/')
        else:
            return render(request, 'registration.html', context={"messages": 'Invalid details'})
    else:
        return render(request, "registration.html")


@login_required(login_url='/user/login/')
@cache_control(no_cache=True, must_revalidate=True)
def index(request, messages=None):
    files = []
    folders = []
    path = []
    fileid = 0
    folderid = 0
    home = STORAGE + '/' + request.user.username
    location = request.session['cdir']
    l = str(location).replace(home, '')
    temp = list(map(str, l.split('/')))
    for t in temp:
        if t != '':
            home = home + '/' + t
        path.append({"label": t, "location": home})
    for file in os.listdir(location):
        dir = os.path.isdir(os.path.join(location, file))
        if dir:
            folders.append({"name": file, "location": location + '/' + file, "id": folderid})
            folderid += 1
        else:
            files.append({"name": file, "size": os.path.getsize(os.path.join(location, file)) / 1000,
                          "location": location + '/' + file, "id": fileid})
            fileid += 1
    folders = sorted(folders, key=lambda k: k['name']);
    files = sorted(files, key=lambda k: k['name']);
    return render(request, 'index.html',
                  context={"files": files, "folders": folders, "path": path, "messages": messages})


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def upload(request):
    if request.method == 'POST':
        filename = request.FILES['myfile'].name
        file = request.FILES['myfile'].read()
        location = request.session['cdir']
        with open(os.path.join(location, filename), 'wb') as temp_file:
            temp_file.write(file)
        return redirect('/user/index/')
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def createfolder(request):
    if request.method == 'POST':
        foldername = request.POST['newfolder']
        location = request.session['cdir']
        fl = os.path.join(location, foldername)
        os.mkdir(fl)
        return redirect('/user/index/')
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def download(request):
    if request.method == 'POST':
        location = request.POST['filename']
        print(location)
        if os.path.exists(location):
            with open(location, 'rb') as file:
                extension = location.split('.')[-1]
                response = HttpResponse(file.read(), content_type=mime.get(extension))
                response['Content-Disposition'] = 'attachment: filename=' + os.path.basename(location)
                return response
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def delete(request):
    if request.method == 'POST':
        location = request.POST['filename']
        try:
            if os.path.exists(location):
                os.remove(location)
                return redirect('/user/index/')
        except:
            return index(request, "Error while deleting !!!")
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def rename(request):
    if request.method == 'POST':
        location = request.POST['filename']
        fname = request.POST['fname']
        destination = request.session['cdir'] + '/' + fname + '.' + location.split('.')[-1]
        if os.path.exists(location):
            os.rename(location, destination)
            return redirect('/user/index/')
        else:
            return Http404('An error has occured')
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def o(request):
    if request.method == 'POST':
        request.session['cdir'] = request.POST['s']
        return redirect('/user/index/')
    else:
        return redirect('/user/login/')


def forgot(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            test = User.objects.get(username=username)
            if test is not None:
                num = random.randint(100000, 999999)
                request.session['otp'] = num
                request.session['username'] = username
                request.session['password'] = password
                mail = details.objects.get(username=username).email
                msg = 'Your OTP for reset password is ' + str(num)
                send_mail('OTP FOR PASSWORD RESET',
                          msg,
                          'noreplycloud123@gmail.com',
                          [mail],
                          fail_silently=False)
                return render(request, 'otp.html')
            else:
                return render(request, 'forgot.html', context={"messages": "Error while updating password"})
        else:
            return render(request, 'forgot.html', context={"messages": "Error while updating password"})
    else:
        return render(request, 'forgot.html')


def validate(request):
    if request.method == 'POST':
        if int(request.session['otp']) == int(request.POST['otp']):
            usr = User.objects.get(username=request.session['username'])
            usr.set_password(request.session['password'])
            usr.save()
            usr = user.objects.get(user_id=request.session['username'])
            usr.password = request.session['password']
            usr.save(update_fields=['password'])
            usr.save()
            usr = details.objects.get(username=request.session['username'])
            usr.password = request.session['password']
            usr.save()
            return render(request, 'login.html', context={"messages": "Password updated successfully"})
        else:
            return render(request, 'otp.html', context={"messages": "Incorrect otp"})
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def frename(request):
    if request.method == 'POST':
        location = request.POST['filename']
        fname = request.POST['fname']
        destination = request.session['cdir'] + '/' + fname
        if os.path.exists(location):
            os.rename(location, destination)
            return redirect('/user/index/')
        else:
            return Http404('An error has occured')
    else:
        return redirect('/user/login/')


@login_required(login_url='/user/login/')
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def fdelete(request):
    if request.method == 'POST':
        location = request.POST['filename']
        try:
            if os.path.exists(location):
                shutil.rmtree(location)
                return redirect('/user/index/')
        except:
            return index(request, "Error while deleting !!!")
    else:
        return redirect('/user/login/')


def profile(request):
    username = request.user.username
    user = details.objects.get(username=username)
    password = user.password
    gender = user.gender
    email = user.email
    bdate = user.bdate
    mono = user.mono
    return render(request, 'profile.html', context={"username": username, "password": password,
                                                    "gender": gender, "email": email,
                                                    "bdate": bdate, "mono": mono})
