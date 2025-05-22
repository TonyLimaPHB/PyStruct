import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Estruturas completas para vários tipos de jogos
ESTRUTURAS = {
    "🕹 Plataforma": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "fonts/"],
        "src": ["__init__.py", "player.py", "level.py", "enemies.py", "physics.py"]
    },
    "🚀 Tiro (Shooter)": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "fonts/"],
        "src": ["__init__.py", "game.py", "player.py", "enemies.py", "bullets.py", "score.py"]
    },
    "🧩 Puzzle": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "fonts/"],
        "src": ["__init__.py", "puzzle.py", "logic.py", "ui.py"]
    },
    "⚔️ RPG": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "fonts/"],
        "src": ["__init__.py", "game.py", "player.py", "enemies.py", "inventory.py", "dialogue.py", "quests.py"]
    },
    "🃏 Cartas": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["cards/", "sounds/"],
        "src": ["__init__.py", "deck.py", "player.py", "ai.py", "game_logic.py"]
    },
    "🏁 Corrida": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["cars/", "tracks/", "sounds/"],
        "src": ["__init__.py", "car.py", "track.py", "physics.py", "hud.py"]
    },
    "🧠 Estratégia": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "maps/"],
        "src": ["__init__.py", "ai.py", "grid.py", "units.py", "turn_manager.py"]
    },
    "🚜 Simulador": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["models/", "ui/", "sounds/"],
        "src": ["__init__.py", "sim_engine.py", "player.py", "world.py"]
    },
    "😱 Horror": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "fonts/", "scripts/"],
        "src": ["__init__.py", "player.py", "monsters.py", "story.py"]
    },
    "🗺 Aventura": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["images/", "sounds/", "maps/"],
        "src": ["__init__.py", "world.py", "player.py", "events.py", "inventory.py"]
    },
    "📚 Livro-Jogo": {
        "": ["main.py", "requirements.txt", "story.json", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "src": ["__init__.py", "story_engine.py", "parser.py"]
    },
    "💬 Visual Novel": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["sprites/", "backgrounds/", "music/"],
        "src": ["__init__.py", "scene.py", "dialogue.py", "choice.py"]
    },
    "🧾 Aventura Interativa (CLI)": {
        "": ["main.py", "requirements.txt", "README.md", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "src": ["__init__.py", "engine.py", "commands.py", "rooms.py", "inventory.py"]
    },
    "📜 Drama Histórico": {
        "": ["main.py", "requirements.txt", "historical_data.json", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "src": ["__init__.py", "timeline.py", "character.py", "events.py"]
    },
    "🕵 Mistério / Detetive": {
        "": ["main.py", "requirements.txt", "cases.json", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "src": ["__init__.py", "clues.py", "interrogation.py", "timeline.py"]
    },
    "👻 Terror Psicológico": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["audio/", "images/", "scripts/"],
        "src": ["__init__.py", "narrative.py", "illusions.py", "sanity.py"]
    },
    "🧙 Fantasia Épica": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["maps/", "races/", "languages/"],
        "src": ["__init__.py", "lore.py", "kingdoms.py", "magic.py", "quests.py"]
    },

    # Novos gêneros adicionados:
    "🎮 Luta (Versus)": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["characters/", "sounds/", "stages/"],
        "src": ["__init__.py", "fighter.py", "battle.py", "ai.py", "hud.py"]
    },
    "🥊 Briga de Rua (Beat'em Up)": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["sprites/", "sounds/", "backgrounds/"],
        "src": ["__init__.py", "player.py", "enemies.py", "combo.py", "levels.py"]
    },
    "🔫 FPS (First-Person Shooter)": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["models/", "weapons/", "sounds/", "maps/"],
        "src": ["__init__.py", "player.py", "weapon.py", "enemy_ai.py", "level.py"]
    },
    "🧗 Metroidvania": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["maps/", "sprites/", "sounds/"],
        "src": ["__init__.py", "player.py", "abilities.py", "map_system.py", "enemy.py"]
    },
    "🧼 Sandbox": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["textures/", "models/", "sounds/"],
        "src": ["__init__.py", "world.py", "editor.py", "inventory.py", "crafting.py"]
    },
    "🐾 Criatura Coletável": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["creatures/", "sounds/", "battles/", "maps/"],
        "src": ["__init__.py", "player.py", "creature.py", "battle.py", "inventory.py"]
    },
    "🕵 Stealth": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["maps/", "characters/", "sounds/"],
        "src": ["__init__.py", "player.py", "ai.py", "visibility.py", "missions.py"]
    },
    "🧬 Sobrevivência": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["textures/", "items/", "sounds/"],
        "src": ["__init__.py", "player.py", "hunger.py", "craft.py", "world.py"]
    },
    "🌍 Mundo Aberto": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["worlds/", "vehicles/", "sounds/"],
        "src": ["__init__.py", "world.py", "player.py", "quests.py", "ai.py"]
    },
    "🏗 Construtor / Base Builder": {
        "": ["main.py", "requirements.txt", "settings.py"],  # settings.py movido para o mesmo nível de main.py
        "assets": ["structures/", "ui/", "sounds/"],
        "src": ["__init__.py", "builder.py", "resources.py", "ai.py", "defense.py"]
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

    lbl_titulo = tk.Label(janela_sobre, text="Criador de Estrutura de Jogos", font=("Segoe UI", 18, "bold"),
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
        "Bem-vindo ao Criador de Estrutura de Jogos!\n\n"
        "Aqui você poderá criar facilmente a estrutura de pastas e arquivos\n"
        "para o seu jogo em Python, escolhendo o tipo de jogo que deseja criar.\n\n"
        "Suporte para plataformas, shooters, RPGs, arcade, quebra-cabeça e muito mais!\n\n"
        "Economize tempo e foque no desenvolvimento do seu jogo.\n\n"
        "Desenvolvido com carinho para todos os devs independentes.\n\n"
        "Tony Lima agradece seu interesse e deseja sucesso nos seus projetos!\n\n"
        "Que seu código seja limpo, seu jogo divertido e sua criatividade sem limites!"
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
    root.title("🎮 Criador de Estrutura de Jogo")
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

    lbl_nome = tk.Label(frame, text="🎮 Nome do Jogo:", bg="#2c2c2c", fg="white", font=("Segoe UI", 12))
    lbl_nome.grid(row=0, column=0, sticky="e", pady=5, padx=10)

    nome_entry = tk.Entry(frame, width=30, font=("Segoe UI", 11))
    nome_entry.grid(row=0, column=1, pady=5, padx=10)

    lbl_tipo = tk.Label(frame, text="📁 Tipo de Jogo:", bg="#2c2c2c", fg="white", font=("Segoe UI", 12))
    lbl_tipo.grid(row=1, column=0, sticky="e", pady=5, padx=10)

    tipo_combobox = ttk.Combobox(frame, values=list(ESTRUTURAS.keys()), width=28, font=("Segoe UI", 10), state="readonly")
    tipo_combobox.grid(row=1, column=1, pady=5, padx=10)
    tipo_combobox.set("🕹 Plataforma")

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
