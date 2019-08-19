function chk_value(form) {
    var txt = "";
    for (var i = 1; i < 7; i++) {
        if (form[i].value == "") {
            alert(form[i].name + " value is empty");
            return false;
        }
        txt += form[i].name + " : " + form[i].value + "\n";
    }

    console.log(txt);
    if (form.password.value != form.password2.value) {
        alert("check password");
        return false;
    }
    if(form.chkOk.checked==false)
    {
        alert("개인정보 취급동의");
        return false;
    }

}