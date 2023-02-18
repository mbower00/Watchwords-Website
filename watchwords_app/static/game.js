function changeColor(to_change, new_color) {
    let text_color = "#FDFFFC"
    if(new_color === "#F1D302"){
        text_color = "#161925"
    }
    to_change.style.backgroundColor = new_color
    to_change.style.color = text_color
}