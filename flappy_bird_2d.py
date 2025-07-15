import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Cores e dimensões
LARGURA, ALTURA = 400, 600
BRANCO = (255, 255, 255)
AZUL = (135, 206, 250)
VERDE = (0, 200, 0)
AMARELO = (255, 255, 0)

# Criar a janela
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Console 2D")

# Relógio
FPS = 60
clock = pygame.time.Clock()

# Pássaro
passaro_x = 50
passaro_y = 300
gravidade = 0.3         # Gravidade suavizada
velocidade = 0
pulo = -6               # Pulo com W
queda = 4               # Descida com S
largura_passaro = 30
altura_passaro = 30

# Cano
cano_largura = 60
cano_espaco = 150
cano_x = LARGURA
cano_altura = random.randint(100, 400)
velocidade_cano = 2.5   # Cano mais lento

# Pontos
pontos = 0
fonte = pygame.font.SysFont("Arial", 24)

# Função para desenhar
def desenhar(passaro_y, cano_x, cano_altura, pontos):
    TELA.fill(AZUL)

    # Pássaro
    pygame.draw.rect(TELA, AMARELO, (passaro_x, passaro_y, largura_passaro, altura_passaro))

    # Canos
    pygame.draw.rect(TELA, VERDE, (cano_x, 0, cano_largura, cano_altura))
    pygame.draw.rect(TELA, VERDE, (cano_x, cano_altura + cano_espaco, cano_largura, ALTURA))

    # Pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    TELA.blit(texto, (10, 10))

    pygame.display.update()

# Loop principal
def main():
    global passaro_y, velocidade, cano_x, cano_altura, pontos
    rodando = True

    while rodando:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    velocidade = pulo  # sobe com W
                elif evento.key == pygame.K_s:
                    velocidade += queda  # desce com S

        # Movimento
        velocidade += gravidade
        passaro_y += velocidade
        cano_x -= velocidade_cano

        # Novo obstáculo
        if cano_x + cano_largura < 0:
            cano_x = LARGURA
            cano_altura = random.randint(100, 400)
            pontos += 1

        # Colisão
        if (passaro_y < 0 or passaro_y + altura_passaro > ALTURA or
            (passaro_x + largura_passaro > cano_x and passaro_x < cano_x + cano_largura and
             (passaro_y < cano_altura or passaro_y + altura_passaro > cano_altura + cano_espaco))):
            print(f"Game Over! Pontuação final: {pontos}")
            pygame.quit()
            sys.exit()

        desenhar(passaro_y, cano_x, cano_altura, pontos)

# Inicia o jogo
main()