package day3

import java.io.File

const val INPUT_FILE = "2024/day3/input.txt"

fun main() {
    val input = File(INPUT_FILE).readText()

    val multiplications = Regex("mul\\((\\d{1,3}),(\\d{1,3})\\)").findAll(input)
        .map { it.groupValues[1].toInt() * it.groupValues[2].toInt() to it.range }
        .sortedBy { it.second.first }

    val part1 = multiplications.sumOf { it.first }
    println("Part 1: $part1")

    val instructionLocations = Regex("(do\\(\\))|(don't\\(\\))").findAll(input)
        .map { it.groupValues[1].isNotEmpty() to it.range }
        .sortedBy { it.second.first }

    val part2 = instructionLocations.sumOf { (enabled, range) ->
        val nextInstruction = instructionLocations.firstOrNull { (_, r) -> range.last < r.first }
        val multiplication = multiplications.firstOrNull { (_, r) -> range.last < r.first }
        if (enabled && multiplication != null && (nextInstruction == null || multiplication.second.last < nextInstruction.second.first))
            multiplication.first
        else 0
    } + multiplications.first().first
    println("Part 2: $part2")

}