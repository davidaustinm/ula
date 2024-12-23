class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def normalize(self):
        if self.p == 0:
            self.q = 1
            return
        if self.q < 0:
            self.p *= -1
            self.q *= -1
        a = self.p
        b = self.q
        while b > 0:
            tmp = b
            b = a%b
            a = tmp
        self.p /= a
        self.q /= a

    def toString(self, mode):
        if self.p == 0:
            return "0"
        if self.q == 1:
            return str(self.p)
        if mode == "inline":
            return str(self.p)+r"/"+str(self.q)
        return r"\frac{"+str(self.p)+"}{"+str(self.q)+"}"

    def add(self, r):
        r = Rational(self.p * r.q + self.q * r.p,
                     self.q * r.q)
        r.normalize()
        return r

    def sub(self, r):
        r = Rational(self.p * r.q - self.q * r.p,
                     self.q * r.q)
        r.normalize()
        return r

    def div(self, r):
        if r.p == 0:
            print "Dividing by zero"
        r = Rational(self.p * r.q, self.q * r.p)
        r.normalize()
        return r

    def mul(self, r):
        r = Rational(self.p * r.p, self.q * r.q)
        r.normalize()
        return r

    def neg(self):
        return Rational(-self.p, self.q)

    def reciprocal(self):
        if self.p == 0:
            print "Seeking reciprocal of zero"
        r = Rational(self.q, self.p)
        r.normalize()
        return r

    def iszero(self):
        return self.p == 0

class Matrix:
    def __init__(self, rows):
        print rows
        newrows = []
        for row in rows:
            newrow = []
            for r in row:
                newrow.append(Rational(r,1))
            newrows.append(newrow)
        self.rows = newrows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def mul(self, m):
        if self.num_cols != m.num_rows:
            print "Dimension mismatch"
        rows = []
        for i in range(self.num_rows):
            row = []
            for j in range(m.num_cols):
                sum = 0
                for k in range(self.num_cols):
                    sum += self.rows[i][k] * m.rows[k][j]
                row.append(sum)
            rows.append(row)
        return Matrix(rows)

    def toLatexString(self):
        s = r"\begin{bmatrix}" + "\n"
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if j == 0:
                    s += "  "
                else:
                    s += r" \amp "
                s += str(self.rows[i][j])
            s += r" \\" + " \n"
        s += r"\end{bmatrix}" + "\n"
        return s

    def clone(self):
        rows = []
        for i in range(self.num_rows):
            rows.append(self.rows[i][:])
        return Matrix(rows)

    def interchange(self, i, j):
        m = self.clone()
        tmp = m.rows[i]
        m.rows[i] = m.rows[j]
        m.rows[j] = tmp
        return m

    def moveToBottom(self, i):
        m = self.clone()
        row = m.rows.pop(i)
        m.rows.append(row)
        return m

    def scaleRow(self, i, s):
        m = self.clone()
        for j in range(m.num_cols):
            m.rows[i] *= s
        return m

    def divideRow(self, i, s):
        m = self.clone()
        for j in range(m.num_cols):
            m.rows[i][j] = m.rows[i][j].div(s)
        return m

    def rowReplacement(self, i, j, s):
        m = self.clone()
        for k in range(m.num_cols):
            m.rows[j][k] = m.rows[j][k].mul(m.rows[i][k])
        return m

    def rref(self):
        m = self.clone()
        col = 0
        row = 0
        while col < m.num_cols:
            pivotrow = row
            while pivotrow < m.num_rows and m.rows[pivotrow][col].iszero():
                pivotrow += 1
            if pivotrow == m.num_rows:
                col += 1
                continue
            if pivotrow != row:
                m = m.interchange(row, pivotrow)
            m = m.divideRow(row, m.rows[row][col])
            for i in range(row + 1, m.num_rows):
                m = m.rowReplacement(row, i, -m.rows[i][col])
            col += 1
            row += 1
            print "---"
            for r in m.rows:
                print r
        row -= 1
        while row > 0:
            pivot = 0
            while pivot < m.num_cols and m.rows[row][pivot] == 0:
                pivot += 1
            for j in range(row - 1, -1, -1):
                m = m.rowReplacement(row, j, -m.rows[j][pivot])
            row -= 1
        print m.toLatexString()
        return m


        
        
