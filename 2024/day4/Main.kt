package day4

import java.io.File

const val INPUT_FILE = "2024/day4/input.txt"

fun main() {
    val input = File(INPUT_FILE).readLines()

    val w = input[0].length
    val h = input.size

    fun get(i: Int, j: Int, dx: Int, dy: Int, k: Int) = input.getOrNull(i + k * dy)?.getOrNull(j + k * dx)

    var part1 = 0
    var part2 = 0
    for (i in 0 until h) {
        for (j in 0 until w) {
            var founds = 0
            for (dx in -1..1) {
                for (dy in -1..1) {
                    if ("XMAS".mapIndexed { k, c -> get(i, j, dx, dy, k) == c }.all { it })
                        part1++

                    if ("MAS".mapIndexed { k, c -> get(i, j, dx, dy, k - 1) == c }.all { it })
                        if (dx != 0 && dy != 0) founds++
                }
            }
            if (founds == 2) part2++
        }
    }
    println("Part 1: $part1")
    println("Part 2: $part2")
}