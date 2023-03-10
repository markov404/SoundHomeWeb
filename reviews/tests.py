
import pytest
import time
import os
import threading
from django.test import TestCase
from io import BytesIO

# Create your tests here.

from reviews.components.translator import Translator
from reviews.components.speecher import Speecher
from reviews.components.speecher import SpeecherBasedYaCloudTech
from reviews.components.speecher import SpeecherModifiedForAsync

@pytest.fixture
def review_text() -> str:
    t_inp = """Burnin’ upends many myths orbiting John Lee Hooker ,
one of the iconic blues musicians of the 20th century. Whether you know either his name or his records, you know his heavy-footed boogie, a rollicking rhythm absorbed and assimilated by such acolytes as George Thorogood and ZZ Top , who once faced a lawsuit from the copyright holder of Hooker’s 1948 breakthrough hit “Boogie Chillen,” claiming the Texas trio ripped off Hooker with their 1973 single “La Grange.” Trending Now The 10 Best Dream Pop Albums ZZ Top won the lawsuit with the court claiming that the rhythm is in the public domain, a ruling that in a perverse way proves how deeply entrenched Hooker’s music is in popular music: It’s impossible to imagine rock’n’roll would sound without him. Hooker’s boogie is so endless, it not only survives long after his death but seemed to exist prior to “Boogie Chillen.” Critics picked up on this eternal essence early in Hooker’s career. Charles Shaar Murray, the author of the definitive John Lee Hooker biography Boogie Man: The Adventures of John Lee Hooker in the American 20th Century , cites the French blues critic Jacques Lemetre as the first to describe the bluesman as “one of the most primitive (from a musical point of view) and, I would say, one of the most African of blues singers” back in 1964, a framing that’s echoed through the years. Calling Hooker’s music primitive obscures a crucial trait, one as essential to understanding his art as his slippery sense of timing: He was a modernist, not a traditionalist. He wasn’t anchored to his birth state of Mississippi: He hightailed it up north as soon as he could, settling in Detroit where he played an electrified update of Delta blues for factory workers in the 1940s. “Boogie Chillen” captured how Hooker played not for a rural audience but for city folk: He bent the bars of a blues vamp, extending the groove to gin up the energy in the room. He didn’t sing laments; he played dance music. This essential distinction comes into sharp relief on 1962’s Burnin’ , a record released in the thick of the folk-blues revolution. In Boogie Man , Murray argues that the 1960 Newport Jazz Festival—the one headlined by Muddy Waters , in a performance distilled on a Chess LP that year—is the point where blues was formally accepted by the “(mainly white) jazz and folk establishments, and its passing as the indigenous voice of the ghetto.” Hooker was hardly above pandering to this trend. Vee-Jay released
an album called The Folk Lore of John Lee Hooker in 1961 and he’d later issue an installment in Chess’ ongoing The Real Folk Blues series in 1966. This isn’t a reflection of Hooker\'s folk roots—indeed, when Riverside approached him to record an album dedicated to Lead Belly , it became clear the bluesman didn’t know the subject of his intended tribute—but rather how he’d go wherever the audience went.To an extent, that\'s what happened with Burnin’ , the fourth album he released on Vee-Jay. Unlike its Windy City rival Chess, Vee-Jay wasn’t primarily known for blues. They specialized in harmony groups, gospel, jazz, and soul, finally landing a major blues artist when the lackadaisical bluesman Jimmy Reed started racking up big hits for the label in the late 1950s. Reed opened the door for Hooker,
whose rambling 1958 hit “I Love You Honey” and lazy 1960 stroll “No Shoes” both demonstrate a clear debt. That’s not the case with Burnin’ . For this session, Vee-Jay hired a group of Detroit musicians
who were toiling away at the various imprints helmed by Berry Gordy, Jr., the impresario who was working hard to keep his Motown label afloat in the early ’60s. Many years later, these musicians would be called the Funk Brothers , a group immortalized in the 2002 documentary Standing in the Shadows of
Motown , but back in 1961 they were struggling to make ends meet, so they were happy to head to Chicago to make a bit more money than they would in Detroit. Hooker had a connection to the Funk Brothers
through Joe Hunter, a pianist who worked the same Motor City circuit as Hooker. This familiarity let
Hooker ease into the rhythms laid down by drummer Benny Benjamin and bassist James Jamerson. The grooves were streamlined when compared to the idiosyncratic beat Hooker played on his own, but they felt
vibrant and vital, pitched halfway between contemporary R&B and the dwindling urban blues market. On
this 60th anniversary reissue, Burnin’ has been remastered by Kevin Gray from the original analog tapes; there’s an audiophile vinyl edition of the stereo mix, along with a CD that has both stereo and mono mixes, plus an alternate of the lively shuffle “Thelma.” Listening now, it’s striking how mid-century modern the album seems. Jamerson and Benjamin keep the beat bouncing, Hunter decorates the margins with runs that also push the rhythm, and guitarist Larry Veeder adds texture and color to Hooker’s bedrock boogie, while Hank Cosby and Andrew “Mike” Terry punctuate riffs, rhythms, and melodies with their greasy saxophone. All the extra instrumentation doesn’t allow Hooker to burrow deep into his grooves, a loss that doesn’t seem especially painful while Burnin’ spins. These club-tested musicians
allow Hooker to take such unexpected detours as vamping on the riff to the Champs’ “Tequila” on “Keep Your Hands to Yourself (She\'s Mine),” which in turn allows him to sing about all manners of eccentricities: He gripes about women processing their hair, swears he’s about to turn over a new leaf now that it’s 1962, implores a paramour “Let’s Make It,” then runs down a list of his domestic needs on “Drug Store Woman,” claiming he’d rather have bathwater waiting than a woman “wearing lipstick and powder, her hair all fixed up.” Anchoring the whole affair is “Boom Boom,” which wasn’t merely his last big hit—it was arguably his greatest. The Funk Brothers help keep his three-chord stomp lean, so slinky and hooky that it reads not as backwoods blues but downtown pop. “Boom Boom” became his only crossover Billboard hit—it peaked at 60, compared to 16 on the R&B chart—eventually making its way to both
the Grammy Hall of Fame and the Rock and Roll Hall of Fame, a position assisted by its embrace by such British Invasion blues-rockers as the Animals and the Yardbirds. ZZ Top surely heard it too: With its “aw-haw-haw-haw” refrain, it’s more clearly an antecedent to “La Grange” than “Boogie Chillen” itself. As pivotal as “Boom Boom” is, Burnin’ isn\'t merely a single surrounded by agreeable also-rans.
The Funk Brothers helped Hooker hone into his modernity, letting him play off contemporary trends in
a way that accentuates how he always existed within the moment, letting the times take shape around his elemental boogie."""
    return t_inp

@pytest.fixture
def revew_text_translated(review_text) -> str:
    trnst = Translator()

    return trnst.translate(review_text)


def test_translator(review_text):
    trnst = Translator()
    
    assert len(review_text) > 5000
    assert isinstance(trnst.translate(review_text), str)


def test_speecher(revew_text_translated):
    spchr = Speecher()

    t0 = time.time()
    file = spchr.get_speech_file_object(revew_text_translated)
    t1 = time.time()
    total = t1 - t0

    print(f'time - {total}')
    assert total < float(100)
    assert isinstance(file, BytesIO)

def test_yandex_based_speecher(revew_text_translated):
    os.environ['YANDEX_CLOUD_IAM_TOKEN'] = 't1.9euelZrInoyUiomJnJ6Ljo_Ml5PHzO3rnpWakYuXzJSMl5SMycidjJmLxpvl8_c1NVJf-e92Rhk6_t3z93VjT1_573ZGGTr-.df4Yp3g4UVoFbJrQAjQyZojZpxl6eV7vxEMdraTbL6BNPJ9eT2_Vl7vnMQIguwfBD2nFS2Rla_RUDkP6CT7ODg'
    os.environ['YANDEX_CLOUD_FOLDER_ID'] = 'b1g5maebo5uupmgv97hb'

   
    def mok_service_side_call_realisation_two(data: list[dict]):
        spchr = SpeecherModifiedForAsync()
        threads = []
        results = [{} for x in data]
        for i, point in enumerate(data):
            text = point['translation']
            nt = threading.Thread(
                target=spchr.get_speech_file_object, 
                args=(text, i, results)
                )
            nt.start()
            threads.append(nt)

        for process in threads:
            process.join()

        del spchr
        
        for rslt, point in zip(results, data):
            point['audio_bytes'] = rslt 
        
        return data[0]['audio_bytes']

    def mok_service_side_call_realisation_one(data: list[dict]):
        spchr = SpeecherBasedYaCloudTech()
        threads = []
        results = [{} for x in data]
        for i, point in enumerate(data):
            text = point['translation']
            nt = threading.Thread(
                target=spchr.get_speech_file_object, 
                args=(text, i, results)
                )
            nt.start()
            threads.append(nt)

        for process in threads:
            process.join()

        del spchr
        
        for rslt, point in zip(results, data):
            point['audio_bytes'] = rslt
        
        return data[0]['audio_bytes']


    _data1 = [{'translation': revew_text_translated}]

    t0 = time.time()
    rslt1 = mok_service_side_call_realisation_one(_data1)
    t1 = time.time()
    total = t1 - t0
    print(f'Time using API - {total}')

    _data2 = [{'translation': revew_text_translated}]
    print(type(rslt1))
    t0 = time.time()
    rslt2 = mok_service_side_call_realisation_two(_data2)
    t1 = time.time()
    total = t1 - t0
    print(f'Time using google DevKit - {total}')

    assert type(rslt1) == type(rslt2)
