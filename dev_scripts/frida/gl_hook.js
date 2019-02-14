var DebugConsolLogEX_ptr = 0x508CD4;

Java.perform(function () {
	console.log("Java side hook");

	var AppStartupRuntimeCall = Java.use("org.ubisoft.UbiAppStartUpRuntime");
	var UbiDebug = Java.use("org.ubisoft.UbiDebug");

	UbiDebug.v.implementation = function(classe, message) {
		send("verbose:::" + classe + ": " + message);
	};

	UbiDebug.e.implementation = function(classe, message) {
		send("error:::" + classe + ": " + message);
	};
	
	UbiDebug.i.implementation = function(classe, message) {
		send("info:::" + classe + ": " + message);
	};
	
	UbiDebug.d.implementation = function(classe, message) {
		send("debug:::" + classe + ": " + message);
	};
	
	UbiDebug.w.implementation = function(classe, message) {
		send("warning:::" + classe + ": " + message);
	};

	AppStartupRuntimeCall.onCreate.implementation = function(activity, bundle) {
		console.log("onCreate got called");
		this.onCreate(activity, bundle);
		
		console.log("Native side hook")
		var lib_base = Process.findModuleByName("libGalaxyLifePocketAdventures.so").base;
		console.log("Lib base address " + lib_base);
		
		// Here we hook the sub that is supposed to log stuff 
		// The second args hold a pointer that point to the log message
		// We simply read and log the message thanks to the frida API
		Interceptor.attach(ptr(lib_base.add(DebugConsolLogEX_ptr + 1)), {
			onEnter: function(args) {
				send("native:::" + Memory.readUtf8String(args[2]) + ': ' + Memory.readUtf8String(args[3]));
			}
		});
	};
});