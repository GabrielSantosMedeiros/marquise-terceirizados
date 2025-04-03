from typing import *

def background_style() -> str:
    return (
        'background-color: #D9D9D9;'
    )


def wireframe_style() -> str:
    return (
        'background-color: #E9ECEF;' + 
        'border-radius: 10px;'
    )

def input_line_style() -> str:
    return (
        'background-color: #E9ECEF;' + 
        'color: #000;' +
        'font-size: 20px;' + 
        'border: none;' + 
        'border-bottom: 1px solid black;' + 
        'border-radius: 0px;'
    )

def simple_button() -> str:
    return (
        '''
            QPushButton {
                padding: 10px; 
                background-color: #D9D9D9; 
                color: #000;
                font-size: 20px;
                font-weight: bold;
                border: none;
                border-radius: 20px;
                text-align: center;
            }
            QPushButton:hover {
                border: 1px solid blue;
            }
            QPushButton:pressed {
                background-color: #E9ECEF;
            }
        '''
    )