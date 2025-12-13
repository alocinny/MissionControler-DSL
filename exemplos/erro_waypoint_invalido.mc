mission "Teste Erro Semantico Waypoint Invalido" {

    settings {
        max_altitude: 30.0
        base_speed: 6.0
        failsafe_battery: 20
    }

    waypoints {
        "Home"          : -27.6037, -48.5191
        "Ponto A"       : -27.5950, -48.5550, 15.0
    }

    start {
        takeoff(10.0)
    }

    task "Ir para ponto que nao existe" {
        goto("Ponto A")
        goto("Ponto X")
        rtl()
    }

    end {
        land()
    }
}