function k1(data) {
	eel.send(data)
}
function exit(){
  	var w = window();
   	w.close();
	eel.ex()
}
function k5() {
	eel.dj()
}
function connect() {
	eel.con()
}
function dconnect() {
	eel.dcon()
}
async function txt() {
            let file = document.getElementById('file-name');
            
            // Call into Python so we can access the file system
            let text = await eel.out()();
            file.innerHTML = text;
        }