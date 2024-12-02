import java.io.File

fun readInput(filename: String): List<List<Int>> = File(filename).readLines()
    .map { Regex("(\\d+)").findAll(it).toList() }
    .map { row -> row.map { it.value.toInt() } }