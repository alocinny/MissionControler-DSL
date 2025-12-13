mission "Teste Erro Semantico Tipo Dado" {

    settings {
        max_altitude: 30.0
        base_speed: 6.0
        failsafe_battery: 20
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Alvo"          : -27.5950, -48.5550, 15.0
    }

    start {
        takeoff("dez")
        speed(5.0)
    }

    task "Missao Normal" {
        goto("Alvo")
        rtl()
    }

    end {
        land()
    }
}