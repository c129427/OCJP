import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

public class DataEHoraJavaTimeExample {
    public static void main(String[] args) {
        System.out.println("=== API de data e hora java.time ===");
        LocalDate inicio = LocalDate.of(2025, 1, 31);
        LocalDate depoisDeUmMes = inicio.plus(Period.ofMonths(1));
        LocalDateTime reuniao = LocalDateTime.of(2025, 6, 15, 14, 30);
        ZonedDateTime reuniaoEmNovaYork = reuniao.atZone(ZoneId.of("America/New_York"));
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("LocalDate representa uma data sem horario: " + inicio.format(formato));
        System.out.println("Adicionar Period de um mes devolve uma nova data: "
                + depoisDeUmMes.format(formato));
        System.out.println("LocalDate original nao foi alterada: " + inicio);
        System.out.println("LocalDateTime sem fuso: " + reuniao);
        System.out.println("ZonedDateTime com fuso: " + reuniaoEmNovaYork);
    }
}
