# Global Redirect

> A new "world-class" website is claiming to have top-tier security worthy of an international stage. Unfortunately for them, their defenses are far from impressive. Show how easy it is to navigate their weaknesses and gain admin access.

Inspect element -> locate script tags shows

```js
function loginAuthenticate(){
    var password = document.getElementById("password");
    var hash = sjcl.hash.sha256.hash(password);
    var hexRepresentation = sjcl.codec.hex.fromBits(hash);
    if (hexRepresentation == "2a70282a868c0ca9e6fe5bb5cf2ac2ea6b523062102bada26fb87091d511e3f1"){
        alert("welcome Home Admin");
        window.location = "./0078f62f00305b73de6ccace8f9fc1f68a8f1dcec865d33fcacbaf255ddefaa7";
    }else{
        alert("Incorrect Password. Please Try Again");
    }
    alert(hash);
}
```

After reading this, realize that you just need to put `/0078f62f00305b73de6ccace8f9fc1f68a8f1dcec865d33fcacbaf255ddefaa7` after the base URL to navigate to the admin page.