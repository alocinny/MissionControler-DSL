mission "Teste Missao Curta" {

    settings {
        max_altitude: 20.0          # metros
        base_speed: 4.0             # m/s
        failsafe_battery: 25        # inteiro de 10 a 30
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Ponto Alvo"    : -27.5950, -48.5550, 15.0
    }

    start {
        takeoff(10.0)
        speed(3.0)
    }

    task "Ida e Retorno" {
        goto("Ponto Alvo")
        hover(2)
        rtl()
    }

    end {
        land()
    }
}