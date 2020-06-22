
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function createFolder(csrftoken) {
    var foldername = prompt("Please enter foldername:");
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/createfolder/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','newfolder');
    file.setAttribute('type','hidden');
    file.setAttribute('value',foldername);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();l̥
}

function download(filename, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/download/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','text');
    file.setAttribute('value',filename);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();
}

function del(filename, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/delete/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','hidden');
    file.setAttribute('value',filename);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();
}

function rename(filename, csrftoken) {
     var fname = prompt("Please enter new name:");
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/rename/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','hidden');
    file.setAttribute('value',filename);
    form.appendChild(file);
    f = document.createElement('input');
    f.setAttribute('name','fname');
    f.setAttribute('type','hidden');
    f.setAttribute('value',fname);
    form.appendChild(f);
    document.body.appendChild(form);
    form.submit();
}

function o(folderlocation, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/open/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','s');
    file.setAttribute('type','hidden');
    file.setAttribute('value',folderlocation);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();
}

function fr(filename, csrftoken) {
    var fname = prompt("Please enter new name:");
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/frename/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','hidden');
    file.setAttribute('value',filename);
    form.appendChild(file);
    f = document.createElement('input');
    f.setAttribute('name','fname');
    f.setAttribute('type','hidden');
    f.setAttribute('value',fname);
    form.appendChild(f);
    document.body.appendChild(form);
    form.submit();
}

function fdel(filename, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/fdelete/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','hidden');
    file.setAttribute('value',filename);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();
}