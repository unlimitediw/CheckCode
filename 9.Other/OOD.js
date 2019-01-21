/**
// construct
var Book = function(id, bookname, price){
	// 私有属性
	var num = 1;
	// 私有方法
	function checkId(){

	};
	// 特权方法
	this.getName = function(){};
	this.getPrice = function(){};
	this.setName = function(name){
		this.bookname = name;
	};
	this.setPrice = function(price){
		this.price = price;
	};
	//对象共有属性
	this.id = id;
	//对象共有方法
	this.copy = function(){};
	//constructor
	this.setName(bookname);
	this.setPrice(price);
}

Book.prototype.display = function(){
	// show this book
}

var book = new Book(10, 'Javascript design pattern',50);
//console.log(book.bookname); //java 设计模式

Book.prototype.isChinese = true;
Book.isRich = true;
Book.resetTime = function(){
	//console.log("haha");
}

//console.log(book.isChinese,book.isRich);
if(Book.isRich){
	Book.resetTime();
}

//闭包
//闭包式有权访问另外一个函数作用域变量的函数，即在一个函数内部创建另外一个函数。
var Bag = (function(){
	//静态私有变量
	var bagNum = 0;
	//静态私有方法
	function checkBag(name){

	}
	//返回构造函数
	return function(newId, newName, newPrice){
		//私有变量
		var name, price;
		//私有方法
		function checkID(id){};
		//特权方法
		this.getName = function(){};
		this.getPrice = function(){};
		this.setName = function(name){
			this.bagname = name;
		};
		this.setPrice = function(price){
			this.price = price;
		};
		//对象共有属性
		this.id = id;
		//对象共有方法
		this.copy = function(){};
		bagNum++;
		if(bagNum > 100) throw new Error('bilibili');
		this.setName(newName);
		this.setPrice(newPrice);
	}

	//构建原型
	_bag.prototype = {
		//静态共有熟悉
		isJSBag : false,
		display : function(){}
	}
	//返回类
	return _bag;
})();

//检查模式
var Keyboard = function(title, time, type){
	if(this instanceof Keyboard){
		this.title = title;
		this.time = time;
		this.type = type;
	}else{
		return new Keyboard(title,time,type)
	}
}

var keyboard = Keyboard('Javascript','2014','js');
//console.log(keyboard);

//window默认为全局变量, 一旦以new声明则不会获取。
//console.log(keyboard.title);
//console.log(keyboard.time);


// 2.3 继承
// 类式继承
function SuperClass(){
	this.superValue = true;
}
// 为父类添加共有方法
SuperClass.prototype.getSuperValue = function(){
	return this.superValue;
};
//声明子类
function SubClass(){
	this.subValue = false;
}
//继承父类
SubClass.prototype = new SuperClass();
SubClass.prototype.getSubValue = function(){
	return this.subValue;
};

var instance = new SubClass();
//console.log(instance.getSuperValue());
//console.log(instance.getSubValue());

//检测实例与继承
//console.log(SubClass instanceof SuperClass);
//console.log(SubClass.prototype instanceof SuperClass);
//console.log(SubClass.prototype instanceof Object);

//由于继承父类，一旦其中一个子实例改变了父类构造函数中的共有属性，则所有子类都会被影响
//解决方案： 构造函数继承
function SuperClass(id){
	this.books = ['alpha','beta','zero'];
	this.id = id;
}

SuperClass.prototype.showBooks = function(){
	console.log(this.books);
};

function SubClass(id){
	//用 SuperClass call(this,..args)的方法新建并继承父类 
	SuperClass.call(this,id);
}

var instance1 = new SubClass(10);
var instance2 = new SubClass(11);

//sinstance1.books.push("gamma");
//console.log(instance1.books,instance1.id);
//console.log(instance2.books,instance2.id);

//组合式继承 类式继承+构造函数继承
//声明父类
function SuperClass(name){
	//值类型共有属性
	this.name = name;
	//引用类型共有属性
	this.books = ["html","css","Javascript"];

	this.getName = function(){
		return this.name;
	};
}

//父类原型共有方法
SuperClass.prototype.getName = function(){
	console.log(this.name);
};
//声明子类
function SubClass(name,time){
	// 1. 构造函数式继承父类name属性
	SuperClass.call(this,name);
	//子类中新增共有属性
	this.time = time;

	this.getTime = function(){
		return this.time;
	};
}

// 2. 类式继承 子类原型继承父类
SubClass.prototype = new SuperClass();
//子类原型方法
SubClass.prototype = new function(){
	console.log(this.time);
};

var instance1 = new SubClass("js",2014)
//instance1.books.push("c++");
//console.log(instance1.books);
var instance2 = new SubClass("cs",2015);
//console.log(instance2.books);


//console.log(instance2.getName());
//console.log(instance2.getTime());
*/
//原型式继承
//是类式继承的一个封装，新new F中无内容所以开销较小，但也有父类共有属性影响的问题。用寄生式继承解决
function inheritObject(o){
	//声明一个过渡函数对象
	function F(){};
	//过渡对象的原型继承父对象
	F.prototype = o;
	//返回过度对象的一个实例，该实例的原型继承了父对象
	return new F();
}
//寄生式继承， 其为对原型继承的二次封装，封装过程中对继承的对象进行了拓展
//声明基对象
var book = {
	name: "is book",
	alikeBook: ["css","c++"]
};

var anotherBook = {
	color : 'blue'
}
function createBook(obj){
	//通过原型继承方式创建新对象
	var o = new inheritObject(obj);
	//拓展对象
	o.getName = function(){
		console.log(name);
	};
	//返回拓展后的新对象
	return o;
}

//寄生组合式继承
function inheritPrototype(subClass,superClass){
	//复制一份父类的原型副本保存在变量中
	var p = inheritObject(superClass.prototype);
	//修正因为重写子类原型导致子类的constructor属性被修改
	p.constructor = subClass;
	//设置子类的原型
	subClass.prototype = p;
}

//test
//定义父类
function SuperClass(name){
	this.name = name;
	this.color = ["r","b","g"];
}

//定义父类原型方法
SuperClass.prototype.getName = function(){
	console.log(this.name);
};
//定义子类
function SubClass(name,level){
	//构造函数继承
	SuperClass.call(this,name);
	//子类新增属性
	this.level = level;
}
//寄生式继承父类原型
inheritPrototype(SubClass,SuperClass);
//子类新增原型方法
SubClass.prototype.getLevel = function(){
	console.log(this.level);
};
//test
var instance1 = new SubClass("js",3);
var instance2 = new SubClass("ml",2);

instance1.color.push("y");
console.log(instance1.color);
console.log(instance2.color);
instance2.getName();
instance2.getLevel();

//多继承
//单继承 属性复制
var extend = function(target, source){
	//遍历源对象中的属性
	for (var property in source){
		target[property] = source[property];
	}
	return target;
};

extend(anotherBook,book);
//console.log(anotherBook.alikeBook);
anotherBook.alikeBook.push("css");
anotherBook.name = 'not a book';
console.log(anotherBook.alikeBook);
//仅仅只是复制
console.log(book.name);
console.log(anotherBook.name);

//多继承 属性复制
//mix 方法将传入的多个对象的属性复制到源对象中，实现对多个对象属性继承
var mix = function(){
	var i = 1,					//从第二个参数起作为被继承的对象
		len = arguments.length,	//获取参数长度
		target = arguments[0],	//第一个对象为目标对象
		arg;					//缓存参数对象
	for(;i < len;i++){
		//缓存当前对象
		arg = arguments[i];
		//遍历被继承对象中的属性
		for(var property in arg){
			//将被继承对象中的属性复制到目标对象中
			target[property] = arg[property];
		}
	}
	return target;
};

//object属性继承

Object.prototype.mix = function(){
	var i = 0,					//从第二个参数起作为被继承的对象
		len = arguments.length,	//获取参数长度
		arg;					//缓存参数对象
	for(;i < len;i++){
		//缓存当前对象
		arg = arguments[i];
		//遍历被继承对象中的属性
		for(var property in arg){
			//将被继承对象中的属性复制到目标对象中
			this[property] = arg[property];
		}
	}
}
