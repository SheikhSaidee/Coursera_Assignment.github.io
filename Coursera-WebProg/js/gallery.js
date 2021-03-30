var nam;
function upDate(previewPic){
    nam=document.getElementById('image').innerHTML;
    document.getElementById('image').style.backgroundImage = 'url('+ previewPic.src + ')';
    document.getElementById('image').innerHTML = previewPic.alt;
}
function unDo(){
    document.getElementById('image').style.backgroundImage="";
    document.getElementById('image').innerHTML=nam;
}