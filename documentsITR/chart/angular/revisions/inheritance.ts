class Report {
    data: Array<string>;

    constructor(data: Array<string>) {
        this.data = data;
    }

    run(): void {
        this.data.forEach((line) => {
            console.log(line);
        });
    }
}

class TabbedReport extends Report {
    headers: Array<string>;
    constructor(headers: string[], values: string[]) {
        super(values);
        this.headers = headers;
    }

    run() {
        console.log(this.headers);
        super.run();
    }
}


var headers: string[] = [
    'first header',
    'second header'
];

var data: string[] = ['Anu', 'Divya', 'Riddhi'];
var r: TabbedReport = new TabbedReport(headers, data);
r.run();