

STYLES = {
    'buttons':"""
QPushButton {
    background-color:none;
    border: .5px solid rgb(254, 0, 57);;  
    color: rgb(254, 0, 57);
    border-radius: 5px;
    font-weight: bold;
    padding: 5px 10px;
}
QPushButton:hover {
    background-color:qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 1 #C0392B,                              
    stop: 0 #E74C3C );
    color:white;
}
QPushButton:pressed {
    background-color: rgb(254, 0, 57);
    color:white;            
}
QPushButton:disabled {
    background-color: none;
    border-color: #aaaaaa;
    color: #666666;
}"""
    
}