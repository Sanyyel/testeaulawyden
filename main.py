from flask import Flask, jsonify
from app import create_app

app = create_app()

if __name__ == "__main__":
    
    app.run(debug=True)

"""
PROJECT Umbrella - Hotel Manager feito por:

Ana Julia Ghirali da Silva 202302378481
Daniel Gomes de Moraes Sanches 202102074721
Leandro Rocha De Sena 202211214981
Leonardo Manente Lourençon 202102074754
Rodrigo Silva Pereira 202208717748
"""