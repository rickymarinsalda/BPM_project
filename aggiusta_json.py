def fix_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json_file.read()

    # Rimuovi eventuali spazi bianchi extra
    data = data.strip()

    # Aggiungi virgole tra gli oggetti
    data = data.replace('}\n{', '},\n{')

    # Aggiungi parentesi quadre per creare un array
    fixed_data = '[' + data + ']'

    # Sovrascrivi il file con i dati corretti
    with open(file_path, 'w') as json_file:
        json_file.write(fixed_data)


# Esegui la correzione
if __name__ == "__main__":
    json_file_path = "Industrial_and_Scientific_adj.json"
    fix_json_file(json_file_path)
