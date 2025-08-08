import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Escolha a pasta que deseja organizar")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "planilhas": [".xlsx", ".xls", ".ods"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "documentos": [".doc", ".docx", ".odt", ".rtf", ".txt", ".md"],
    "apresentações": [".ppt", ".pptx", ".odp"],
    "áudio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma"],
    "vídeo": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "executáveis": [".exe", ".msi", ".bat", ".sh", ".apk", ".bin"],
    "código_fonte": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".cs", ".php", ".rb", ".go", ".ts", ".swift", ".kt"],
    "bancos_de_dados": [".sql", ".db", ".sqlite", ".accdb"],
    "modelos_3d": [".obj", ".fbx", ".stl", ".dae", ".3ds", ".blend"],
    "fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "outros": [".iso", ".dll", ".log", ".ini", ".tmp"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")