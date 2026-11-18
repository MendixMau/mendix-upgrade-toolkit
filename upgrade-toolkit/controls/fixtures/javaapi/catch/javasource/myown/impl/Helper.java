package myown.impl;

// not a Java action: its own context() is not the removed API
public class Helper {
	private final Object ctx = null;
	Object context() { return ctx; }
	Object use() { return context(); }
}
