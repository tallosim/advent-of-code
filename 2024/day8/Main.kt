package day8

import common.permutations
import java.io.File

data class Position(val x: Int, val y: Int) : Comparable<Position> {
    operator fun plus(other: Position) = Position(x + other.x, y + other.y)
    override fun compareTo(other: Position) = x.compareTo(other.x).let { if (it == 0) y.compareTo(other.y) else it }
}

data class Enviroment(val map: List<List<Char>>) {
    private val width = map[0].size
    private val height = map.size

    val antennas = mutableMapOf<Char, MutableList<Position>>()

    init {
        for (i in 0 until height) {
            for (j in 0 until width) {
                val c = map[i][j]
                if (c.isLetterOrDigit()) antennas.getOrPut(c) { mutableListOf() } += Position(i, j)
            }
        }
    }

    fun isInside(pos: Position) = pos.x in 0 until height && pos.y in 0 until width
}

const val INPUT_FILE = "2024/day8/input.txt"

fun main() {
    val map = File(INPUT_FILE).readLines().map { it.toList() }

    val env = Enviroment(map)

    val part1 = mutableSetOf<Position>()
    for ((_, positions) in env.antennas) {
        for ((pos1, pos2) in positions.permutations(2)) {
            Position(2 * pos2.x - pos1.x, 2 * pos2.y - pos1.y).takeIf { env.isInside(it) }?.let(part1::add)
        }
    }
    println("Part 1: ${part1.size}")

    val part2 = mutableSetOf<Position>()
    for ((_, positions) in env.antennas) {
        for ((pos1, pos2) in positions.permutations(2)) {
            var pos = pos2
            while (env.isInside(pos)) {
                part2 += pos
                pos += Position(pos2.x - pos1.x, pos2.y - pos1.y)
            }
        }
    }
    println("Part 2: ${part2.size}")
}