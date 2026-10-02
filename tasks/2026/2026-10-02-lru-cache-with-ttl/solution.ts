export class LRUCache<K, V> {
  private capacity: number;
  private defaultTTL: number;
  private map: Map<K, Node<K, V>>;
  private head: Node<K, V>;
  private tail: Node<K, V>;

  constructor(capacity: number, defaultTTL: number) {
    this.capacity = capacity;
    this.defaultTTL = defaultTTL;
    this.map = new Map();
    this.head = new Node<K, V>(null as unknown as K, null as unknown as V, 0);
    this.tail = new Node<K, V>(null as unknown as K, null as unknown as V, 0);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get size(): number {
    return this.map.size;
  }

  get(key: K): V | undefined {
    const node = this.map.get(key);
    if (!node) return undefined;
    if (this.isExpired(node)) {
      this.removeNode(node);
      this.map.delete(key);
      return undefined;
    }
    this.moveToHead(node);
    return node.value;
  }

  set(key: K, value: V, ttl?: number): void {
    const expiry = Date.now() + (ttl ?? this.defaultTTL);
    const node = this.map.get(key);
    if (node) {
      node.value = value;
      node.expiry = expiry;
      this.moveToHead(node);
      return;
    }
    const newNode = new Node(key, value, expiry);
    this.addToHead(newNode);
    this.map.set(key, newNode);
    if (this.map.size > this.capacity) {
      const lru = this.tail.prev!;
      this.removeNode(lru);
      this.map.delete(lru.key);
    }
  }

  delete(key: K): boolean {
    const node = this.map.get(key);
    if (!node) return false;
    this.removeNode(node);
    this.map.delete(key);
    return true;
  }

  private isExpired(node: Node<K, V>): boolean {
    return Date.now() >= node.expiry;
  }

  private addToHead(node: Node<K, V>): void {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next!.prev = node;
    this.head.next = node;
  }

  private removeNode(node: Node<K, V>): void {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
  }

  private moveToHead(node: Node<K, V>): void {
    this.removeNode(node);
    this.addToHead(node);
  }
}

class Node<K, V> {
  key: K;
  value: V;
  expiry: number;
  prev: Node<K, V> | null;
  next: Node<K, V> | null;

  constructor(key: K, value: V, expiry: number) {
    this.key = key;
    this.value = value;
    this.expiry = expiry;
    this.prev = null;
    this.next = null;
  }
}
