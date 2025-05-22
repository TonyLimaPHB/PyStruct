import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Estruturas para vários tipos de softwares (modos de software)
ESTRUTURAS = {
    "🖥 Aplicativo Desktop": {
        "": ["main.py", "requirements.txt", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "icons/", "styles/"],
        "src": ["__init__.py", "app.py", "ui.py", "logic.py"]
    },
    "🌐 Aplicação Web": {
        "": ["app.py", "requirements.txt", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de app.py
        "static": ["css/", "js/", "images/"],
        "templates": ["base.html", "index.html", "layout.html"],
        "src": ["__init__.py", "routes.py", "models.py", "forms.py", "utils.py"]
    },
    "📊 Biblioteca / API": {
        "": ["setup.py", "README.md", "LICENSE", "settings.py"],  # settings.py movido para o mesmo nível de setup.py
        "docs": ["index.md", "usage.md"],
        "src": ["__init__.py", "core.py", "helpers.py", "exceptions.py"]
    },
    "🛠 Ferramenta de Linha de Comando (CLI)": {
        "": ["main.py", "README.md", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "docs": ["usage.md", "changelog.md"],
        "src": ["__init__.py", "cli.py", "commands.py", "utils.py"]
    },
    "🤖 Automação / Script": {
        "": ["automation.py", "config.yaml", "README.md"],
        "scripts": ["build.sh", "deploy.sh", "test.sh"],
        "logs": []
    },
    "📱 Aplicativo Mobile": {
        "": ["app.py", "requirements.txt", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de app.py
        "assets": ["images/", "sounds/", "fonts/"],
        "src": ["__init__.py", "main.py", "screens.py", "utils.py"]
    },
    "🧪 Projeto Científico": {
        "": ["experiment.py", "requirements.txt", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de experiment.py
        "data": ["raw/", "processed/"],
        "notebooks": ["analysis.ipynb", "visualization.ipynb"],
        "src": ["__init__.py", "models.py", "utils.py", "plotting.py"]
    },
    "💾 Banco de Dados / ETL": {
        "": ["main.py", "config.ini", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "scripts": ["extract.py", "transform.py", "load.py"],
        "logs": []
    },
    "🔧 Plugin / Extensão": {
        "": ["plugin.py", "manifest.json", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de plugin.py
        "assets": ["icons/", "locales/"],
        "src": ["__init__.py", "handlers.py", "ui.py"]
    }
}


def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def criar_estrutura(base_path, estrutura):
    log = []
    for pasta, arquivos in estrutura.items():
        pasta_path = os.path.join(base_path, pasta)
        os.makedirs(pasta_path, exist_ok=True)
        if pasta != "":
            log.append(f"├── {pasta}/")
        for arquivo in arquivos:
            if arquivo.endswith('/'):
                subpasta_path = os.path.join(pasta_path, arquivo[:-1])
                os.makedirs(subpasta_path, exist_ok=True)
                log.append(f"│   ├── {arquivo}")
            else:
                arquivo_path = os.path.join(pasta_path, arquivo)
                if not os.path.exists(arquivo_path):
                    with open(arquivo_path, 'w', encoding='utf-8') as f:
                        f.write("")
                log.append(f"│   ├── {arquivo}")
    return log

def tela_sobre():
    janela_sobre = tk.Tk()
    janela_sobre.title("ℹ️ Sobre")
    janela_sobre.configure(bg="#1e1e1e")
    largura, altura = 500, 320
    centralizar_janela(janela_sobre, largura, altura)
    janela_sobre.resizable(False, False)

    lbl_titulo = tk.Label(janela_sobre, text="🖥️ Criador de Estrutura de Softwere", font=("Segoe UI", 18, "bold"),
                          fg="white", bg="#1e1e1e")
    lbl_titulo.pack(pady=10)

    lbl_dev = tk.Label(janela_sobre, text="Desenvolvedor: Tony Lima\nContato: +55 86 98119-2287",
                       font=("Segoe UI", 12), fg="white", bg="#1e1e1e")
    lbl_dev.pack(pady=5)

    frame_texto = tk.Frame(janela_sobre, width=460, height=140, bg="black")
    frame_texto.pack(pady=10)

    canvas = tk.Canvas(frame_texto, width=460, height=140, bg="black", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    texto_scroll = (
    "Bem-vindo ao Criador de Softweres!\n\n"
    "Aqui você poderá criar facilmente a estrutura de pastas e arquivos\n"
    "para o seu software em Python, escolhendo o tipo de software que deseja criar.\n\n"
    "Suporte para aplicativos, ferramentas, sistemas, utilitários, automações e muito mais!\n\n"
    "Economize tempo e foque no desenvolvimento do seu software.\n\n"
    "Desenvolvido com carinho para todos os devs independentes.\n\n"
    "Tony Lima agradece seu interesse e deseja sucesso nos seus projetos!\n\n"
    "Que seu código seja limpo, seu software funcional e sua criatividade sem limites!"
)


    texto_id = canvas.create_text(230, 140, text=texto_scroll, fill="white",
                                 font=("Segoe UI", 11), width=440, anchor="n")

    def scroll_text():
        canvas.move(texto_id, 0, -1)
        pos = canvas.coords(texto_id)
        if pos[1] < -250:
            canvas.coords(texto_id, 230, 140)
        janela_sobre.after(50, scroll_text)

    scroll_text()

    def abrir_interface():
        janela_sobre.destroy()
        criar_interface()

    btn_ok = tk.Button(janela_sobre, text="OK", command=abrir_interface,
                       bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"), relief="flat", padx=20, pady=5)
    btn_ok.pack(pady=10)

    janela_sobre.mainloop()

def criar_interface():
    root = tk.Tk()
    root.title("🖥️ Criador de Estrutura de Softwere")
    root.configure(bg="#1e1e1e")
    largura, altura = 500, 320
    centralizar_janela(root, largura, altura)
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 11, "bold"), background="#4CAF50", foreground="white")
    style.configure("TCombobox", padding=5)

    frame = tk.Frame(root, bg="#2c2c2c", padx=20, pady=20, bd=2, relief="ridge")
    frame.pack(expand=True)  # expand para ocupar espaço e centralizar verticalmente

    # Centralizar usando grid com sticky='nsew' e coluna única centralizada
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    lbl_nome = tk.Label(frame, text="️🖥 Nome do Softwere:", bg="#2c2c2c", fg="white", font=("Segoe UI", 12))
    lbl_nome.grid(row=0, column=0, sticky="e", pady=5, padx=10)

    nome_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
    nome_entry.grid(row=0, column=1, pady=5, padx=10)

    lbl_tipo = tk.Label(frame, text="📁 Tipo de Softwere:", bg="#2c2c2c", fg="white", font=("Segoe UI", 12))
    lbl_tipo.grid(row=1, column=0, sticky="e", pady=5, padx=10)

    tipo_combobox = ttk.Combobox(frame, values=list(ESTRUTURAS.keys()), width=28, font=("Segoe UI", 10), state="readonly")
    tipo_combobox.grid(row=1, column=1, pady=5, padx=10)
    tipo_combobox.set("🖥 Aplicativo Desktop")

    botao_criar = tk.Button(frame, text="🚀 Criar Projeto", command=lambda: criar_projeto(nome_entry, tipo_combobox, root),
                            bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"),
                            relief="flat", padx=10, pady=5)
    botao_criar.grid(row=2, column=0, columnspan=2, pady=20, sticky='nsew')

    # Configurar grid da root para centralizar frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frame.grid_rowconfigure(3, weight=1)

    root.mainloop()

def criar_projeto(nome_entry, tipo_combobox, root):
    nome_jogo = nome_entry.get().strip()
    tipo_jogo = tipo_combobox.get()
    if not nome_jogo:
        messagebox.showwarning("⚠️ Erro", "Por favor, insira o nome do jogo.")
        return
    if tipo_jogo not in ESTRUTURAS:
        messagebox.showwarning("⚠️ Erro", "Selecione um tipo de jogo válido.")
        return

    pasta_destino = filedialog.askdirectory(title="Escolha onde salvar o projeto")
    if not pasta_destino:
        return

    projeto_path = os.path.join(pasta_destino, nome_jogo)
    try:
        os.makedirs(projeto_path, exist_ok=True)
    except Exception as e:
        messagebox.showerror("❌ Erro", f"Falha ao criar pasta do projeto:\n{e}")
        return

    log_estrutura = criar_estrutura(projeto_path, ESTRUTURAS[tipo_jogo])

    try:
        with open(os.path.join(projeto_path, "estrutura.txt"), "w", encoding="utf-8") as f:
            f.write(f"Estrutura criada:\n{projeto_path}/\n")
            for linha in log_estrutura:
                f.write(f"{linha}\n")
    except Exception as e:
        messagebox.showerror("❌ Erro", f"Falha ao criar arquivo de log:\n{e}")
        return

    messagebox.showinfo("✅ Sucesso", f"O projeto '{nome_jogo}' foi criado com sucesso!")

if __name__ == "__main__":
    tela_sobre()
