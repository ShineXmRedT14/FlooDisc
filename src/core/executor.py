import logging
import asyncio
import json
import aiofiles

from urllib.parse import urlparse
from pathlib import Path
from src.config.visual import banner, cls, inittool
from src.config.cnf import obj
from src.core.params import PackArg, HTTPArg, SaveArg
from src.core.utils import ferr, pather
from src.core.exceptions import ExecutorInitError, ExecutorCallError, AsyncHandlerError, JsonSaveError

class executor:
    def __init__(
        self,
        source: str | None = None,
        destination: str | None = None,
        url: str | None = None,
        timeout: int | float | None = None,
        allow: bool | None = None,
        args: PackArg | None = None,
        tasks: int | None = None
        ):
        self.source = source
        self.destination = destination
        self.url = url
        self.timeout = timeout
        self.allow = allow
        self.args = args
        self.tasks = tasks
        self.dirs = [403, 401, 429, 451]

    def __call__(
        self,
        timeout: int | float | None = None,
        allow: bool | None = None,
        url: str | None = None,
        args: PackArg | None = None,
        source: str | None = None,
        destination: str | None = None,
        tasks: int | None = None
        ):
        try:
            if timeout is not None:self.timeout = timeout
            if allow is not None:self.allow = allow
            if url is not None:self.url = url
            if args is not None:self.args = args
            if source is not None:self.source = source
            if destination is not None:self.destination = destination
            if tasks is not None:self.tasks = tasks
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise ExecutorCallError(message=e)

    async def savehttp(self, status: int | None, rate: int | None, param: HTTPArg) -> None:
        try:
            data = {}

            if status is None or rate is None:
                data["rate"] = "5000+ (no rate limit)"
                data["status"] = "Any (without ban statuses)"
            data["rate"] = rate
            data["status"] = status
            data.setdefault("options", {})
            data["options"]["url"] = param.url
            data["options"]["timeout"] = param.timeout
            data["options"]["allow"] = param.allow
            data["options"]["tasks"] = param.tasks

            jsn = json.dumps(data, indent=4, ensure_ascii=False)
            parse = urlparse(param.url)
            hostn = parse.hostname
            paths = parse.path.strip("/")

            nurl = f"{hostn.replace('.', '-')}-{paths.replace('/', '-')}".strip("-")
            rnpath = f"info/{nurl}.json"

            async with aiofiles.open(obj.path(rpath=rnpath), "w", encoding="utf-8") as f:
                await f.write(jsn)

        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise JsonSaveError(message=e)

    def savepkt(self, status: int | None, rate: int | None, param: SaveArg) -> None:
        try:
            data = {}

            if status is None or rate is None:
                data["rate"] = "5000+ (no rate limit)"
                data["status"] = "Any (without ban statuses)"
            data["rate"] = rate
            data["status"] = status
            data.setdefault("options", {})
            data["options"]["source"] = param.source
            data["options"]["destination"] = param.destination
            data["options"]["type"] = param.type

            jsn = json.dumps(data, indent=4, ensure_ascii=False)
            rnpath = f"info/{param.destination}.json"

            with open(obj.path(rpath=rnpath), "w", encoding="utf-8") as f:
                f.write(jsn)

        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise JsonSaveError(message=e)

    def cstatus(self, item: int) -> dict:
        try:
            for status in self.dirs:
                if item == status:
                    return {"bool": True, "status": status}

            return {"bool": False, "status": None}
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            return {"bool": False, "status": None}

    async def AsyncHandler(self) -> None:
        try:
            import aiohttp

            async with aiohttp.ClientSession() as session:
                from src.core.network import HTTPReq

                context = HTTPArg()
                context.allow = self.allow
                context.url = self.url
                context.timeout = self.timeout

                rate = 1
                obj = HTTPReq(session=session, args=context)

                while True:
                    if rate >= 5000:
                        await self.savehttp(status=None, rate=None, param=context)
                        break

                    if self.tasks - rate > 0:
                        tasks = [obj.request() for _ in range(rate)]
                        statuses = await asyncio.gather(*tasks)

                        for item in statuses:
                            data = self.cstatus(item=item["status"])
                            if data["bool"]:
                                index = statuses.index(item)
                                if index > 0:
                                    index -= 1
                                    ctime = statuses[index]["time"] - statuses[0]["time"]
                                    k = round(1/ctime, 10)
                                    crate = index*k

                                    await self.savehttp(status=data["status"], rate=crate, param=context)
                                else:
                                    await self.savehttp(status=data["status"], rate=rate, param=context)

                                break

                        if rate < 100:rate += 1
                        elif rate < 300:rate += 10
                        elif rate >= 1000:rate += 100
                    else:
                        counts = round(rate/self.tasks)
                        times = rate

                        for _ in range(counts):
                            tasks = [obj.request() for _ in range(self.tasks)]
                            statuses = await asyncio.gather(*tasks)

                            for item in statuses:
                                data = self.cstatus(item=item["status"])
                                if data["bool"]:
                                    index = statuses.index(item)
                                    if index > 0:
                                        index -= 1
                                        ctime = statuses[index]["time"] - statuses[0]["time"]
                                        k = round(1/ctime, 10)
                                        crate = index*k

                                        await self.savehttp(status=data["status"], rate=crate, param=context)
                                    else:
                                        await self.savehttp(status=data["status"], rate=rate, param=context)

                                    break

                            times - self.tasks

                        tasks = [obj.request() for _ in range(self.tasks)]
                        statuses = await asyncio.gather(*tasks)

                        for item in statuses:
                            data = self.cstatus(item=item["status"])
                            if data["bool"]:
                                index = statuses.index(item)
                                if index > 0:
                                    index -= 1
                                    ctime = statuses[index]["time"] - statuses[0]["time"]
                                    k = round(1/ctime, 10)
                                    crate = index*k

                                    await self.savehttp(status=data["status"], rate=crate, param=context)
                                else:
                                    await self.savehttp(status=data["status"], rate=rate, param=context)

                                break

                        if rate < 100:rate += 1
                        elif rate < 300:rate += 10
                        elif rate >= 1000:rate += 100

                    await asyncio.sleep(1)
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise AsyncHandlerError(message=e)

    def graph(self) -> None:
        try:
            cls()
            banner()
            inittool()
        except Exception as e:logging.critical(ferr(e), exc_info=True)

    def GenArg(self) -> SaveArg:
        try:
            context = SaveArg()
            context.source = self.source
            context.destination = self.destination

            if self.args.tonp == 1:context.type = "TCP"
            elif self.args.tonp == 2:context.type = "UDP"
            elif self.args.tonp == 3:context.type = "ICMP"
            else:context.type = "Unknown"

            return context
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise Exception(e)

    def packets(self) -> None:
        try:
            self.graph()

            from src.core.network import PackRegs
            import time as tm

            obj = PackRegs(src=self.source, dst=self.destination, params=self.args)
            rate = 1

            while True:
                if rate >= 5000:
                    self.savepkt(status=None, rate=None, param=self.GenArg())
                    break

                packet = obj.regpkt()
                obj.sendpkt(packet=packet, rate=rate)
                status = obj()

                data = self.cstatus(item=status)

                if data["bool"]:
                    self.savepkt(status=data["status"], rate=rate, param=self.GenArg())
                    break

                if rate < 100:rate += 1
                elif rate < 300:rate += 10
                elif rate >= 1000:rate += 100

                tm.sleep(1)
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise ExecutorInitError(message=e)
    def requests(self) -> None:
        try:
            self.graph()
            asyncio.run(self.AsyncHandler())
        except Exception as e:
            logging.critical(ferr(e), exc_info=True)
            raise ExecutorInitError(message=e)