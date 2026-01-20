class Slab:
    def __init__(self, object_size, objects_per_slab):
        self.object_size = object_size
        self.objects_per_slab = objects_per_slab

        self.memory = [None] * objects_per_slab
        self.bitmap = [False] * objects_per_slab

    def alloc(self):
        for i in range(self.objects_per_slab):
            if not self.bitmap[i]:
                self.bitmap[i] = True
                self.memory[i] = f"obj_{id(self)}_{i}"
                return self.memory[i]
        return None

    def free(self, obj):
        for i in range(self.objects_per_slab):
            if self.memory[i] == obj:
                self.bitmap[i] = False
                self.memory[i] = None
                return True
        return False

    def is_full(self):
        return all(self.bitmap)

    def contains(self, obj):
        return obj in self.memory

class SlabCache:
    def __init__(self, object_size, objects_per_slab):
        self.object_size = object_size
        self.objects_per_slab = objects_per_slab
        self.slabs = []

    def alloc(self):
        for slab in self.slabs:
            if not slab.is_full():
                return slab.alloc()

        new_slab = Slab(self.object_size, self.objects_per_slab)
        self.slabs.append(new_slab)
        return new_slab.alloc()

    def free(self, obj):
        for slab in self.slabs:
            if slab.contains(obj):
                return slab.free(obj)
        print("Błąd: nie znaleziono obiektu")
        return False

if __name__ == "__main__":
    cache = SlabCache(object_size=32, objects_per_slab=3)

    a = cache.alloc()
    b = cache.alloc()
    c = cache.alloc()  
    d = cache.alloc() 

    print(a, b, c, d)

    cache.free(b)

    e = cache.alloc()
    print(e)
