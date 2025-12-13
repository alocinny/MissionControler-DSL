mission "Teste Missao Loop" {

    settings {
        max_altitude: 15.0          # metros
        base_speed: 5.0             # m/s
        failsafe_battery: 30        # inteiro de 10 a 30
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Inspecao A"    : -27.5910, -48.5510, 10.0
        "Inspecao B"    : -27.5920, -48.5520, 10.0
    }

    start {
        takeoff(8.0)
        speed(4.0)
    }

    task "Ciclo de Inspecao" {
        # Primeira Passagem
        goto("Inspecao A")
        hover(3)
        goto("Inspecao B")
        hover(3)

        # Segunda Passagem
        goto("Inspecao A")
        hover(3)
        goto("Inspecao B")
        hover(3)
    }

    task "Voltar para Base" {
        rtl()
    }

    end {
        land()
    }
}