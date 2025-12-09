mission "Teste Missao Longa" {

    settings {
        max_altitude: 40.0          # metros
        base_speed: 8.0             # m/s
        failsafe_battery: 15        # inteiro de 10 a 30
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Ponto 1"       : -27.5800, -48.5600, 35.0
        "Ponto 2"       : -27.5750, -48.5500, 30.0
        "Ponto Check"   : -27.5850, -48.5400, 25.0
        "Ponto Final"   : -27.5900, -48.5300, 20.0
    }

    start {
        takeoff(20.0)
        speed(7.0)
    }

    task "Percurso Longo" {
        goto("Ponto 1")
        goto("Ponto 2")
        hover(5)
        speed(5.0) # Mudança de velocidade no meio da missão
        goto("Ponto Check")
    }

    task "Retorno Programado" {
        goto("Ponto Final")
        hover(10) # Sobrevôo mais longo para coleta de dados
        rtl()
    }

    end {
        land()
    }
}